from datetime import datetime

def time_until_new_year():
    now = datetime.now()
    next_year = now.year + 1
    new_year = datetime(next_year, 1, 1)
    
    time_left = new_year - now
    
    days = time_left.days
    hours = time_left.seconds // 3600
    minutes = (time_left.seconds % 3600) // 60
    seconds = time_left.seconds % 60
    
    return days, hours, minutes, seconds

# Запуск программы
days, hours, minutes, seconds = time_until_new_year()
print(f"До Нового года осталось: {days} дней, {hours} часов, {minutes} минут, {seconds} секунд")
