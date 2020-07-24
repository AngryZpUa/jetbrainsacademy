scores = input().split()
# put your python code here
if scores.count("I") < 3:
    print("You won")
    print(scores.count("C"))
else:
    print("Game over")
    c_counter = 0
    i_counter = 0
    for char in scores:
        if char == 'C':
            c_counter += 1
        else:
            i_counter += 1
        if i_counter == 3:
            break
    print(c_counter)
