import json
filename = 'numbers.json'
with open(filename) as f:
    fav_number = json.load(f)
print(f'Your favorite number is {fav_number}.')