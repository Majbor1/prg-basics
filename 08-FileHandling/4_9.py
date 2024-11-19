import csv

with open("it_company.csv", 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if row[2] == "Graphic Designer":
            print(f"{row[1]} {row[0]}, {row[3]}")