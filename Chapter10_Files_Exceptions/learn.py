with open('whativelearned.txt') as file:
    text = file.readlines()


for tex in text:
    if tex == "i love python!!":
        print(tex.upper().strip())
        continue
    print(tex.strip())
