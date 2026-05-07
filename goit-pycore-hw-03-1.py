from datetime import datetime

def get_days_from_today(date):
    try:
         target_date = datetime.date(datetime.strptime(date, '%Y-%m-%d'))
         current_date = datetime.now().date()
         difference = current_date - target_date
         return difference.days
    except ValueError:
        return "Wrong format"
    else:
        return difference.days
print(get_days_from_today('2026-08-10'))