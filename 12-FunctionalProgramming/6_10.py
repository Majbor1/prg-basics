import matplotlib.pyplot as plt

data = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

cities = list(map(lambda x: x[0], data.items()))
temps = list(map(lambda x: x[1], data.items()))


plt.bar(cities, temps, color="skyblue")

plt.title("Temperatures in cities")
plt.xlabel("Cities")
plt.ylabel("Temperatures")

plt.show()