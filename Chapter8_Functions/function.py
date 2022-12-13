import math

def greet_user(name):
    """Displays simple greeting"""
    print(f"Hey there, {name.upper()}! Wonderful day today, isn't it!")

def favorite_book(title):
    print(f"One of my favorite books is \"{title.title()}\"!")

def quadForm(a, b, c):
    d = (b**2) - (4*a*c)
    sol1 = (-b-math.sqrt(d))/(2*a)
    sol2 = (-b+math.sqrt(d))/(2*a)
    return sol1, sol2

def describe_pet(animal = 'dog', name = 'filo'):
    print(f"I have a {animal.upper()}, and their name is {name.title()}!")

def make_shirt(size = 'large', message = 'i love python!'):
    print(f"Shirt size: {size.upper()}")
    print(f"Message: {message.title()}")

def fullName(first, last, middle = ''):
    if middle:
        fullName = f"{first} {middle} {last}".title()
    else:
        fullName = f"{first} {last}".title()
    return fullName

def build_person(firstname, lastname, age = 'NA'):
    person = {
        'first': firstname,
        'last': lastname,
        'full': f"{firstname} {lastname}".title()
    }
    
    if age:
        person['age'] = age
    return person



def askName():
    active = True
    while active:
        print("What is your name?")
        response = input("First: ")
        if response == 'quit':
            active = False
            break
        firstName = response
        response = input("Last: ")
        if response == 'quit':
            active = False
            break
        lastName = response
        print(f"Your fullname is {fullName(firstName, lastName)}")


def completeTasks(tasks):
    completedTasks = []
    while tasks:
        currentTask = tasks.pop()
        print(f"I am {currentTask}!")
        completedTasks.append(currentTask)
    return completedTasks

tasks = ['taking out the trash', 'feeding the dog', 'doing my homework', 'cleaning my room']

print(f"Tasks: {tasks}")
completedTasks = completeTasks(tasks)
print(f"Completed Tasks: {completedTasks}")
print(f"Tasks: {tasks}")




        