import matplotlib.pyplot as plt

olimpic = [{"country":"Denmark","gold":2,"silver":4,"bronze":6},
{"country":"Finland","gold":5,"silver":0,"bronze":4},
{"country":"USA","gold":12,"silver":5,"bronze":11},
{"country":"Peru","gold":0,"silver":1,"bronze":7}]

country = list(map(lambda x: x['country'], olimpic))
medals = list(map(lambda x: x['gold']+x['silver']+x['bronze'], olimpic))

plt.bar(country, medals, color="black")

plt.title("Amount of medals")

plt.xlabel("Countries")
plt.ylabel("Medals")

plt.show()