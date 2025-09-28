# Day 18
# https://www.100daysofcode.io/learn/python/day-18

def list_sum(list):
    total = 0
    for item in list:
        total += item
    print(f"total = {total}")

list_sum([1, 2, 3, 4, 5])