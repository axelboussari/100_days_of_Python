# Day 6: Functions and Code Reusability

# Default and Keyword Arguments
def greet_user(name="Guest"):
    print(f"Hello, {name}")
    
# Function with Return Value

def area_rectangle(length, width):
    return length * width

#Variable Scope

name = "Alice"

def modify_name():
    global name
    name = "Bob"
    print("Inside function:", name)

modify_name()

print("Outside function:", name)