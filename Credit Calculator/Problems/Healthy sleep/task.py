A = int(input())
B = int(input())
H = int(input())
if A < H < B:
    print("Normal")
if A > H:
    print("Deficiency")
if B < H:
    print("Excess")
