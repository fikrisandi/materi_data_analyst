# Python untuk DA — Master Cheatsheet

## Variables & Types

```python
n = 10                     # int
x = 1.5                    # float
s = "Halo"                 # string
b = True                   # bool
none = None
```

## String

```python
f"Halo {nama}, umur {umur}"
"Halo".upper(), .lower(), .strip(), .replace("a","b")
" ".join(["a", "b"])           # "a b"
"a,b,c".split(",")              # ["a","b","c"]
"abc".startswith("a"), .endswith("c")
len("abc")                       # 3
```

## List

```python
xs = [1, 2, 3]
xs[0], xs[-1], xs[0:2]
xs.append(4), xs.extend([5, 6])
xs.remove(2), del xs[0]
len(xs), 2 in xs
sorted(xs), xs.sort()
```

## Dict

```python
d = {"a": 1, "b": 2}
d["a"], d.get("c", default=0)
d["c"] = 3
"a" in d
d.keys(), d.values(), d.items()
{**d1, **d2}                   # merge
```

## Set

```python
s = {1, 2, 3}
s.add(4)
s & t      # intersection
s | t      # union
s - t      # difference
```

## Conditions

```python
if x > 5:
    ...
elif x > 0:
    ...
else:
    ...

# Ternary
y = "Big" if x > 5 else "Small"
```

## Loops

```python
for i in range(10):
    ...

for item in xs:
    ...

for i, item in enumerate(xs):
    ...

for k, v in d.items():
    ...

for a, b in zip(xs, ys):
    ...

while x > 0:
    x -= 1
```

## Comprehension

```python
[x**2 for x in range(10)]
[x for x in xs if x > 5]
{i: i**2 for i in range(5)}
{x for x in xs}
```

## Functions

```python
def f(a, b=10, *args, **kwargs):
    return a + b

# Lambda
square = lambda x: x ** 2

# Type hints
def add(a: int, b: int) -> int:
    return a + b
```

## File I/O

```python
with open("file.txt") as f:
    content = f.read()

with open("out.txt", "w") as f:
    f.write("hello")

import json
with open("data.json") as f:
    data = json.load(f)
```

## Error Handling

```python
try:
    risky()
except ValueError as e:
    print(e)
except Exception:
    print("error")
finally:
    cleanup()

assert x > 0, "x harus positif"
```

## Class (Basic)

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name}"

p = Person("Andi", 25)
p.greet()
```

## Modules

```python
import math
from math import sqrt, pi
import pandas as pd     # alias convention
```

## Common Standard Library

```python
import datetime
datetime.date.today()
datetime.datetime.now()

import os
os.getcwd(), os.listdir(), os.path.join("a", "b")

import re
re.search(r"pattern", text)
re.findall(r"\d+", "abc 123 def")

import random
random.choice([1, 2, 3])
random.randint(1, 10)

import json
json.loads(string), json.dumps(dict)
```

## DA-Specific Aliases

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
```
