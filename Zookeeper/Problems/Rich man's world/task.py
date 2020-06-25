deposit = int(input())
years = 0
while deposit < 700000:
    years += 1
    deposit = int(deposit * 7.1 / 100 + deposit)
print(years)
