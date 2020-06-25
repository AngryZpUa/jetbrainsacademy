# put your python code here
days = int(input())
food_cost_per_day = int(input())
fly_ticket = int(input())
hotel_per_day = int(input())
result = food_cost_per_day * days + fly_ticket * 2 + hotel_per_day * (days - 1)
print(result)
