a = input()
b = str.lower(a)[::-1]
if a == b:
    print("Palindrome")
else:
    print("Not palindrome")
