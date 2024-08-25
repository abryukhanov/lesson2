def month_to_season(month):
    
    if month in [12, 1, 2]:
        return 'Зима'
    elif month in [3, 4, 5]:
        return 'Весна'
    elif month in [6, 7, 8]:
        return 'Лето'
    elif month in [9, 10, 11]:
        return 'Осень'
    else:
        raise ValueError(f"Некорректный месяц: {month}")

while True:
    try:
        month = int(input("Введите номер месяца: "))
        season = month_to_season(month)
        print(f"Месяц {month} относится к сезону {season}.")
    except ValueError as e:
        print(e)
    except KeyboardInterrupt:
        break