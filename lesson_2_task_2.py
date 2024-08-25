def is_year_leap(year):

    return year % 4 == 0

year = 2022
is_leap_year = is_year_leap(year)
print(f"год {year}: {is_leap_year}")