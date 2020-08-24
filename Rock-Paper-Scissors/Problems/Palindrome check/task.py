# please work with the preset variable `word`
forward = word[::-1]
backward = word[0::1]

if forward == backward:
    print("Yes")
else:
    print("No")