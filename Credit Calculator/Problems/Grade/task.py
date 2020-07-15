grade = int(input())
max_grade = int(input())
percent = int(grade * 100 / max_grade)
if percent < 60:
    print("F")
elif 60 <= percent < 70:
    print("D")
elif 70 <= percent < 80:
    print("C")
elif 80 <= percent < 90:
    print("B")
elif 90 <= percent <= 100:
    print("A")
