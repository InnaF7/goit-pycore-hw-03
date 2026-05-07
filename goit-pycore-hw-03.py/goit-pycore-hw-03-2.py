import random

def get_numbers_ticket(min, max, quantity):
    min >= 1
    max <=1000
    min < quantity <= max
    return sorted (random.sample(range(1,1000), 6))

lottery_numbers = get_numbers_ticket(1, 1000, 6)
print("Ваші лотерейні числа:",lottery_numbers)
