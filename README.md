# timer-py
Simple timer class

Example usage

```python
from pyext.util.timer import Timer

with Timer("1. HELLO WORLD"):
    print("Stuff...")

with Timer("2. HELLO WORLD", f_print=Timer.mute):
    print("Stuff...")

with Timer("3. HELLO WORLD", f_print=Timer.highlight('** ')):
    print("Stuff...")

```

Output 

```
1. HELLO WORLD started at 10:31:00
Stuff...
1. HELLO WORLD took 0:00:00
Stuff...
** 3. HELLO WORLD started at 10:31:00
Stuff...
** 3. HELLO WORLD took 0:00:00
```
