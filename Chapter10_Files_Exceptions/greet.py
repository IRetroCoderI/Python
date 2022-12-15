import json

file = 'username.json'
with open(file, 'r') as file_object:
    username = json.load(file_object)
    print(f"Welcome back, {username.title()}")