from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    today = datetime.now()
    start_day = today + timedelta(days=1)
    end_day = start_day + timedelta(days=7)
    
    birth_week = {day: [] for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']}
    
    for user in users:
        user_birthday = user['birthday'].replace(year=today.year)
        
        if user_birthday.month == 2 and user_birthday.day == 29 and not today.year % 4 == 0:
            user_birthday = user_birthday.replace(day=28)
        if start_day <= user_birthday < end_day:
            if user_birthday.weekday() == 5 or user_birthday.weekday() == 6:
                birth_day = 'Monday'
            else:
                birth_day = user_birthday.strftime('%A')
            birth_week[birth_day].append(user['name'])
    
    for day, names in birth_week.items():
        if names:
            print(f"{day}: {', '.join(names)}")


get_birthdays_per_week([
        {"name": "Test Test", "birthday": datetime(1955, 2, 24)},
        {"name": "Test1 Test1", "birthday": datetime(1955, 2, 25)},
        {"name": "Test2 Test2", "birthday": datetime(1955, 2, 26)},
        {"name": "Test3 Test3", "birthday": datetime(1955, 2, 27)},
        {"name": "Test4 Test4", "birthday": datetime(1956, 2, 29)},
        {"name": "Test5 Test5", "birthday": datetime(1955, 2, 28)},
    ])