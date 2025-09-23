# Day14
# https://www.100daysofcode.io/learn/python/day-14

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0):
            print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

is_leap_year(2021)