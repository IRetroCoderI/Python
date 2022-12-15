file = 'write.txt'

with open(file, 'w') as file_object:
    file_object.write("I love python!!\n")
    file_object.write("I love to build videogames!!\n")

with open(file, 'a') as file:
    file.write("also heres a new line!!")