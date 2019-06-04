from pyext.util.timer import Timer

with Timer("1. HELLO WORLD"):
    print("Stuff...")

with Timer("2. HELLO WORLD", f_print=Timer.mute):
    print("Stuff...")

with Timer("3. HELLO WORLD", f_print=Timer.highlight('** ')):
    print("Stuff...")
