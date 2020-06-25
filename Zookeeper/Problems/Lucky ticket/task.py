# Save the input in this variable
ticket = int(input())

# Add up the digits for each half
num11 = ticket // 100000
ticket = ticket % 100000
num12 = ticket // 10000
ticket = ticket % 10000
num13 = ticket // 1000
ticket = ticket % 1000
num21 = ticket // 100
ticket = ticket % 100
num22 = ticket // 10
num23 = ticket % 10
half1 = num11 + num12 + num13
half2 = num21 + num22 + num23

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")