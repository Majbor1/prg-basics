import json

def number_of_rooms(data):
    rooms = 0
    for datum in data['reservations']:
        rooms += 1
        
    return rooms

def number_of_rooms_paid(data):
    rooms = 0
    for datum in data['reservations']:
        if datum['paid']:
            rooms += 1
        
    return rooms

def number_of_rooms_unpaid(data):
    rooms = 0
    for datum in data['reservations']:
        if datum['paid'] == False:
            rooms += 1
        
    return rooms

def value_of_paid(data):
    value = 0
    for datum in data['reservations']:
        if datum['paid']:
            value = datum['price_per_night'] * datum['nights']
        
    return value

def value_of_unpaid(data):
    value = 0
    for datum in data['reservations']:
        if datum['paid'] == False:
            value = datum['price_per_night'] * datum['nights']
        
    return value

with open('reservations.json', 'r', encoding='utf-8') as file:
    content = json.load(file)
    

msg = f"""
Number of rooms: {number_of_rooms(content)}
Number of paid reservations: {number_of_rooms_paid(content)}
Number of unpaid reservations: {number_of_rooms_unpaid(content)}
Total value of paid reservations: {value_of_paid(content)}
Total value of unpaid reservations: {value_of_unpaid(content)}
"""

print(msg)