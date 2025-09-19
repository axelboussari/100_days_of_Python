#Day07: Lists and Tuples

def create_list():
    fruits = ["apple", "banana", "cherry", "date"]
    return fruits

#create_list()

def change_item_value(fruits):
    fruits = create_list()
    fruits[1:3] = ["watermelon", "black"]
 #   print(fruits)
    return fruits
#change_item_value(create_list())

def append_item(fruits):
    fruits = create_list()
    fruits.append("orange")
    # print(fruits)
    return fruits

# append_item(create_list())

def insert_item(fruits):
    fruits = create_list()
    fruits.insert(1, "kiwi")
    print(fruits)
    return fruits

# insert_item(create_list())

def remove_item(fruits):
    fruits = create_list()
    fruits.remove("banana")
    print(fruits)
    return fruits  

# remove_item(create_list())

#Looping through a list

def loop_list(fruits):
    fruits = create_list()
    [print(fruit) for fruit in fruits]

# loop_list(create_list())


#TUPLES

def create_tuple():
    computers = ("Dell", "HP", "Apple", "Asus")
    print(computers)
    return computers
# create_tuple()

def access_tuple(computers):
    computers = create_tuple()
    print(computers[-3:-2])
    return computers
# access_tuple(create_tuple())

def tuple_operations(computers):
    computers = create_tuple()
    print(computers * 2)
    print(computers + ("Acer", "Lenovo"))
    return computers

tuple_operations(create_tuple())
