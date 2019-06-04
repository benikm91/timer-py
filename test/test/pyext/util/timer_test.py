from pyext.util.timer import Timer

with Timer("1. HELLO WORLD"):
    print("WHAT")

with Timer("2. HELLO WORLD", f_print=Timer.mute):
    print("WHAT")

with Timer("3. HELLO WORLD", f_print=print):
    pass
