import time

msg = "hello world\n"


#print(msg)
msg = "\"hello there!!\"\n" #using quotes in python be like
#print(msg)

first_name = "ada"
last_name = "lovelace"
full_name = first_name + last_name
name = f"{first_name} {last_name}"


#print(full_name.upper())
#print(name.lower())


hello_msg = f"Hello, {name.upper()}, how are you today?"
#print(hello_msg)

name = "{} {}".format(first_name, last_name)
#print(name)

print("\t{} \n\t\t{}".format(first_name, last_name.upper()))


langList = "Languages:\n\tJavaScript\n\tJava\n\tC"


name1 = "jesus"
name2 = "jesus    "

if name1 == name2.rstrip(): #rstrip gets rid of right whitespace
    print("True")
else:
    print("false")