# Day 16
# https://www.100daysofcode.io/learn/python/day-16

def is_palindrome(chaine):
    
    if chaine.lower() == chaine[::-1].lower():
        return True
    else:
        return False
    
    
print(is_palindrome("ann"))
        