import json
filename = 'numbers.json'
try:
    with open(filename) as f:
        fav_number = json.load(f)
except FileNotFoundError:
    fav_number = int(input('What is your favorite number? '))
    with open(filename, 'w') as f:
        json.dump(fav_number, f)
    print('We remember your favorite number.')
else:
    print(f'Your favorite number is {fav_number}.')