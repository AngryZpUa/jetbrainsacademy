# put your python code here
hour1 = int(input())
minute1 = int(input())
seconds1 = int(input())
hour2 = int(input())
minute2 = int(input())
seconds2 = int(input())
result = (hour2 - hour1) * 3600 + (minute2 - minute1) * 60 + seconds2 - seconds1
print(result)
