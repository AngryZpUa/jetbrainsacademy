string = input()
float_list = []
while string != '.':
    float_list.append(float(string))
    string = input()
minimal = float_list[0]
for i in float_list:
    if minimal > i:
        minimal = i
print(minimal)
