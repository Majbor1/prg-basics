import csv

with open("clothing.csv", 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        if float(row[5]) < 60 and int(row[6]) < 40:
            print(*row)