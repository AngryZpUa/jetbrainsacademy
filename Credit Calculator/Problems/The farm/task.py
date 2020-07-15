money = int(input())
if money >= 6769:
    print(str(money // 6769) + " sheep")
elif money >= 3848:
    if money // 3848 > 1:
        print(str(money // 3848) + " cows")
    else:
        print("1 cow")
elif money >= 1296:
    if money // 1296 > 1:
        print(str(money // 1296) + " pigs")
    else:
        print("1 pig")
elif money >= 678:
    if money // 678 > 1:
        print(str(money // 678) + " goats")
    else:
        print("1 goat")
elif money >= 23:
    if money // 23 > 1:
        print(str(money // 23) + " chickens")
    else:
        print("1 chicken")
else:
    print("None")
