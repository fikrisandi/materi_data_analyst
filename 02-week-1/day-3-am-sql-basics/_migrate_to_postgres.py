"""Migrate SQLite kopi_kita.db ke PostgreSQL.

Pakai saat sampai Week 2 Day 4 (SQL Advanced di PostgreSQL).

Prasyarat:
- PostgreSQL jalan di localhost:5432 (Docker / Supabase / native)
- pip install psycopg2-binary

Usage:
    python _migrate_to_postgres.py \\
        --pg-host localhost --pg-port 5432 \\
        --pg-user postgres --pg-pass savvys2026 \\
        --pg-db kopi_kita
"""

import argparse
import sqlite3
import sys
from pathlib import Path

SQLITE_DB = Path(__file__).parent / "data" / "kopi_kita.db"


def main(args):
    try:
        import psycopg2
    except ImportError:
        print("Install psycopg2 dulu: pip install psycopg2-binary")
        sys.exit(1)

    # Read from SQLite
    sqlite_conn = sqlite3.connect(SQLITE_DB)
    sqlite_conn.row_factory = sqlite3.Row
    print(f"Reading from: {SQLITE_DB}")

    # Connect to Postgres
    pg_conn = psycopg2.connect(
        host=args.pg_host, port=args.pg_port,
        user=args.pg_user, password=args.pg_pass,
        database=args.pg_db,
    )
    pg_cur = pg_conn.cursor()
    print(f"Connected to PostgreSQL: {args.pg_host}:{args.pg_port}/{args.pg_db}")

    # Drop existing & recreate schema
    pg_cur.execute("""
        DROP TABLE IF EXISTS transaksi CASCADE;
        DROP TABLE IF EXISTS pelanggan CASCADE;
        DROP TABLE IF EXISTS menu CASCADE;
        DROP TABLE IF EXISTS cabang CASCADE;

        CREATE TABLE cabang (
            id_cabang VARCHAR(10) PRIMARY KEY,
            nama_cabang VARCHAR(100),
            kota VARCHAR(50),
            jam_buka VARCHAR(10),
            jam_tutup VARCHAR(10)
        );

        CREATE TABLE menu (
            id_menu VARCHAR(10) PRIMARY KEY,
            nama_menu VARCHAR(100),
            kategori VARCHAR(50),
            harga INTEGER,
            hpp INTEGER
        );

        CREATE TABLE pelanggan (
            id_pelanggan VARCHAR(10) PRIMARY KEY,
            nama VARCHAR(100),
            no_hp VARCHAR(20),
            kota_asal VARCHAR(50),
            tanggal_join DATE,
            membership VARCHAR(20)
        );

        CREATE TABLE transaksi (
            id_transaksi VARCHAR(20) PRIMARY KEY,
            tanggal DATE,
            id_cabang VARCHAR(10) REFERENCES cabang(id_cabang),
            id_pelanggan VARCHAR(10) REFERENCES pelanggan(id_pelanggan),
            id_menu VARCHAR(10) REFERENCES menu(id_menu),
            qty INTEGER,
            harga_satuan INTEGER,
            total INTEGER,
            metode_bayar VARCHAR(20)
        );
    """)
    pg_conn.commit()
    print("Schema created.")

    # Copy data
    for table in ["cabang", "menu", "pelanggan", "transaksi"]:
        rows = list(sqlite_conn.execute(f"SELECT * FROM {table}"))
        if not rows:
            continue
        cols = rows[0].keys()
        placeholders = ",".join(["%s"] * len(cols))
        sql = f"INSERT INTO {table} ({','.join(cols)}) VALUES ({placeholders})"
        for row in rows:
            pg_cur.execute(sql, tuple(row))
        pg_conn.commit()
        print(f"  {table}: {len(rows)} rows migrated.")

    sqlite_conn.close()
    pg_conn.close()
    print("\nMigration complete!")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--pg-host", default="localhost")
    p.add_argument("--pg-port", default="5432")
    p.add_argument("--pg-user", default="postgres")
    p.add_argument("--pg-pass", default="savvys2026")
    p.add_argument("--pg-db", default="kopi_kita")
    main(p.parse_args())
