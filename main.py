from datetime import datetime

def get_days_from_today(date):
   
    try:
        target_date = datetime.strptime(date, '%Y-%m-%d')
        
        current_date = datetime.today()
        
        difference = current_date - target_date
        
        return difference.days
        
    except ValueError:
        
        return "Помилка: Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'."

print(get_days_from_today("2026-08-10")) 
