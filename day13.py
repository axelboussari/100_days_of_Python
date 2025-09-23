# Day13
# https://www.100daysofcode.io/learn/python/day-13

def largest_three_numbers(a, b, c):
    if a > b:
        if a >= c:
            print(f"{a} is the largest number.\n")
        else:
            print(f"{c} is the largest number.\n")
    elif b > a:
        if (b >= c):
            print(f"{b} is the largest number.\n")
        else:
            print(f"{c} is the largest number.\n")
    elif c > a:
        if c > b:
            print(f"{c} is the largest number.\n")
    else:
        print("All numbers are equal.")

#largest_three_numbers(10, 20, 30)