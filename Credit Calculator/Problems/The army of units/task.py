units = int(input())
if units < 1:
    print("no army")
elif units <= 9:
    print("few")
elif units <= 49:
    print("pack")
elif units <= 499:
    print("horde")
elif units <= 999:
    print("swarm")
else:
    print("legion")
