import json
fav_number = int(input('What is your favorite number? '))
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(fav_number, f)
print('We remember your favorite number.')