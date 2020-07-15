jack_age = int(input())
alex_age = int(input())
lana_age = int(input())
if jack_age < alex_age and jack_age < lana_age:
    print(str(jack_age))
elif alex_age < jack_age and alex_age < lana_age:
    print(str(alex_age))
else:
    print(str(lana_age))
