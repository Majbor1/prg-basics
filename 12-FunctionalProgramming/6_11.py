test_results = [
   {"name":"Peter","result":27},
   {"name":"Anna","result":63},
   {"name":"Robert","result":92},
   {"name":"Paul","result":46},
   {"name":"Barbara","result":52}]

res = list(filter(lambda x: 50 <= x["result"] <= 70, test_results))

for i in res:
    print(i["name"])