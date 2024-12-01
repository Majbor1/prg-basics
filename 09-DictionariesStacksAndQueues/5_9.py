import csv

province_dict = {}
with open('province.csv', 'r', encoding="utf-8") as province_file:
    csv_reader = csv.reader(province_file)
    for row in csv_reader:
        letter, province = row
        province_dict[letter] = province

vehicle_count = {}
for province in province_dict.values():
    vehicle_count[province] = 0
    
with open('vehicle.txt', 'r') as vehicle_file:
    for vehicle in vehicle_file:
        first_letter = vehicle[0]
        if first_letter in province_dict:
            province = province_dict[first_letter]
            vehicle_count[province] += 1
            
for province, count in vehicle_count.items():
    print(f"{province}: {count}")