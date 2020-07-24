# The following code is needed for us to check your answer, do not modify it, please.
students = json.loads(input())
Belov = students['Belov']
Smith = students['Smith']
Sarada = students['Sarada']

# Your code here. Work with the variables 'Belov', 'Smith', and 'Sarada'
my_set = set()
for i in Belov:
    my_set.add(i)
for i in Smith:
    my_set.add(i)
for i in Sarada:
    my_set.add(i)
print(len(my_set))
