# Day 8 - Sets and dictionnary
#https://www.100daysofcode.io/learn/python/sets-and-dictionary

def create_set():
    colors = {"red", "blue", "green", "yellow"}
    return colors

# create_set()

def add_in_set(colors):
    colors = create_set()
    colors.add("purple")
    print(colors)
    return colors

def remove_from_set(colors):
    colors = create_set()
    colors.remove("blue")
    print(colors)
    return colors

def difference_sets():
    set1 = {"red", "blue", "green", "yellow"}
    set2 = {"blue", "black", "white"}
    diff = set2.difference(set1)
    print(diff)
    return diff

def intersection_sets():
    set1 = {"red", "blue", "green", "yellow"}
    set2 = {"blue", "black", "white"}
    inter = set1.intersection(set2)
    print(inter)
    return inter

def union_sets():
    set1 = {"red", "blue", "green", "yellow"}
    set2 = {"blue", "black", "white"}
    uni = set1.union(set2)
    print(uni)
    return uni

def loop_set(colors):
    colors = create_set()
    for color in colors:
        print(color)
    return colors

def dictionnary_create():
    student = {
        "name": "John",
        "age": 25
    }
    print(student)
    return student

def access_dictionnary(student):
    student = dictionnary_create()
    print(student.get("name"))
    return student

def update_dictionnary(student):
    student = dictionnary_create()
    student["age"] = 26
    student["city"] = "New York"
    print(student)
    return student

def remove_dictionnary_item(student):
    student = dictionnary_create()
    student.pop("age")
    print(student)
    return student

def loop_on_dictionnary(student):
    student = dictionnary_create()
    for key, value in student.items():
        print(f"{key}: {value}")
    return student
