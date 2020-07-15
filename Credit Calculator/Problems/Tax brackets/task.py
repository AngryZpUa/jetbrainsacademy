money = int(input())
result = "The tax for {income} is {percent}%. That is {calculated_tax} dollars!"
if 0 <= money <= 15527:
    percentage = 0
    tax = str(round(money * percentage / 100))
    print(result.format(income=str(money), percent=str(percentage), calculated_tax=tax))
elif 15528 <= money <= 42707:
    percentage = 15
    tax = str(round(money * percentage / 100))
    print(result.format(income=str(money), percent=str(percentage), calculated_tax=tax))
elif 42708 <= money <= 132406:
    percentage = 25
    tax = str(round(money * percentage / 100))
    print(result.format(income=str(money), percent=str(percentage), calculated_tax=tax))
else:
    percentage = 28
    tax = str(round(money * percentage / 100))
    print(result.format(income=str(money), percent=str(percentage), calculated_tax=tax))
