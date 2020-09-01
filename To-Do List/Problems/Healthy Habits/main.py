# the list "walks" is already defined
# your code here
total_distance = 0
for day in walks:
    total_distance += day["distance"]
print(total_distance // 7)
