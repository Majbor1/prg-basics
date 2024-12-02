import json

with open('vote.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

person_name = input("Name of the person you are voting for: ")

if person_name in data:
    data[person_name] += 1
else:
    data[person_name] = 1
        
with open('vote.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)

