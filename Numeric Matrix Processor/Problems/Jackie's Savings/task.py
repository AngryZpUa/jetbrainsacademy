def final_deposit_amount(*interest, amount=1000):
    interests = [int(x) for x in interest]
    for i in interests:
        amount *= 1 + i / 100
    return round(amount, 2)
