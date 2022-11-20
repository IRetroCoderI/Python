

squares = [value**2 for value in range(1,11)]
print(squares)


for i in range(1,21):
    print(i, end= ", ")

print("\n")
million = [i for i in range(1, 1_000_001)]
print(f"Min:  {min(million)}")
print(f"Max:  {max(million)}")
sum = sum(million)
print(f"Sum of a million ints is {sum}")


oddNums = [i for i in range(1, 20, 2)] #1 through 20, every 2 nums, so odd nums in this case
print(oddNums)

threes = [i for i in range(3, 30, 1*3)] #3 to 30, every multiple of 3
print(f"Threes: {threes}")


cubes = []
for i in range(1, 11):
    cubes.append(i**3)

print(f"Cubes: {cubes}")