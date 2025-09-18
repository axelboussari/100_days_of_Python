# If-else Statements #
# Write a program that takes a number as input and checks if it is even or odd.

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
    
# Write a program that takes an age as input and determines if the person is a child, teenager, adult, or senior citizen. 
age = int(input("Enter your age: "))
if age >= 18 and age <= 65:
    print("You are an adult.\n")
elif age > 65:
    print("You are a senior citizen.\n")
elif age >= 13 and age < 18:
    print("You are a teenager.\n")
else:
    print("You are a child.\n")
    
# Nested If-else Statements #
# Using nested if-else, write a program that takes three numbers as input and determines the largest among them.
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter one more number: "))

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
# For Loops #
# Write a program to calculate the sum of all numbers up to the given input number.

n = int(input("Enter a number: "))

total = 0
for i in range(n):
    total += i + 1
print(f"The sum of all numbers up to {n} is {total}.")


# While Loops #
# Write a program to calculate the factorial of a given number.

n = int(input("Enter a number: "))
factorial = 1
i = n

while i >= 1:
    factorial *= i
    i -= 1
print(f"The factorial of {n} is {factorial}.")