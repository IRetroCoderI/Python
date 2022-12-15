with open('secretmessage.txt') as file_object:
    contents = file_object.readlines()


str = ' '
for content in contents:
    str += content.strip()

print(str)