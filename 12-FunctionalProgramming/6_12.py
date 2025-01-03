olimpic = [{"country":"Denmark","gold":2,"silver":4,"bronze":6},
{"country":"Finland","gold":5,"silver":0,"bronze":4},
{"country":"USA","gold":12,"silver":5,"bronze":11},
{"country":"Peru","gold":0,"silver":1,"bronze":7}]

at_least_10 = list(filter(lambda x: x['gold']+x['silver']+x['bronze'] >= 10, olimpic))

print("COUNTRIES WITH AT LEAST 10 MEDALS")
for i in at_least_10:
    print(f"{i['country']}: {i['gold']}, {i['silver']}, {i['bronze']}")