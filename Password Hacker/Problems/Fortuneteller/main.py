# put your code here
input_str = input()
total_sum = 0
my_generator = (0 + int(x) for x in input_str)
print(sum(my_generator))
