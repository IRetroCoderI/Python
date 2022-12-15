#use a variable to represent a person's name, and print a message to that person. 
# your message should be simple, such as:
#  "hello Eric, would you like to learn some python today??"

name = "eric"
message = f"Hello {name.upper()}, would you like to learn some Python today?"

print(message)


#name = input("What is your name?")
#print(f"Name cases:\n\t{name.upper()}\n\t{name.lower()}\n\t{name.title()}")


author = "albert einstein"
quote = "Learn from yesterday, live for today, hope for tomorrow."
message =f"{author.title()} once said, \"{quote}\"" 
print(message)