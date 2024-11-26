countries = [
{"name":"Poland", "population":38000000},
{"name":"Italy", "population":51000000},
{"name":"Hungary", "population":13000000},
{"name":"Germany", "population":122000000},
{"name":"Monaco", "population":60000},
]

print(f"COUNTRY | POPULATION")
for i in countries:
    print(f"{i["name"]} | {i["population"]}")