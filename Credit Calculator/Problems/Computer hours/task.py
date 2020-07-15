# Make sure your output matches the assignment *exactly*
pc_hours = int(input())
if pc_hours < 2:
    print("That seems reasonable")
elif pc_hours < 4:
    print("Do you have time for anything else?")
else:
    print("You need to get outside more!")
