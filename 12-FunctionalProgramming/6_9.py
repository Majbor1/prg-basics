cities = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

result = list(filter(lambda x: cities[x] >= 0, cities))

print(*result)