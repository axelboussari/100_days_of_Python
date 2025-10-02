# Day 20
# https://www.100daysofcode.io/learn/python/day-20

def calculate_fibonnacci():
    limit = int(input("Enter a number for the limit fo fibonnacci:"))
    i = 1
    j = 1
    tour = 0
    fibonnacci_list = []
    fibonnacci_list.append(i)
    fibonnacci_list.append(j)
    
    while tour <= limit:
        total = i + j
        fibonnacci_list.append(total)
        i = j
        j = total
        tour += 1
    print(fibonnacci_list)

calculate_fibonnacci()