
message = "If you tell us who you are, we can personalize the message you see."
message += "\nWhat is your first name?\n"

name = input(message)

greeting = f"Hello, {name}"

print(greeting)

age = int(input(f"How old are you, {name}?\n"))
print(f"{name} is {age} years old!")