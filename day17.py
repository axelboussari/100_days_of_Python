# Day17
# https://www.100daysofcode.io/learn/python/day-17

def count_vowel(chaine):
    mylist = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
    count = 0
    
    for i in chaine:
        for li in mylist:
            if li in i:
                count += 1
    print(f"count = {count}")
count_vowel("Asake Uhh Yeahh")