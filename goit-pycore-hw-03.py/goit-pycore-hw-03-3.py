import re

def normalize_phone(phone_number):
    cleaned = re.sub(r'[^\d+]', '', phone_number)
    if not cleaned.startswith('+'):
        if cleaned.startswith('38'):
            cleaned = '+' + cleaned
        else:
            cleaned = '+38' + cleaned
    return cleaned

raw_phone_number = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ", ]
normalize_phone_numbers = [normalize_phone(num) for num in raw_phone_number]
print("Нормалізовані номери телефонів для SMS-розсилки:", normalize_phone_numbers)
