import json

nums = [2,3,5,7,11,13]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(nums, f)