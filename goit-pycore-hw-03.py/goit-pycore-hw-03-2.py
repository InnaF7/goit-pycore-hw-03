import random

def get_numbers_ticket(min, max, quantity):
    return sorted (random.sample(range(min, max), quantity))

lottery_numbers = get_numbers_ticket(1, 1000, 6)
print("Ваші лотерейні числа:",lottery_numbers)
