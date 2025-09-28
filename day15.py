# Day 15
# https://www.100daysofcode.io/learn/python/day-15

def compute_factorial(number):
    result = 1
    print(f"before = {result}")
    i = 1
    while i <= number:
        result = result * i
        i += 1
    print(result)
        
compute_factorial(5)