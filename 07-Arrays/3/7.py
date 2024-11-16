names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
count = []

for name in names:
    counter = 0
    for i in range(len(name)):
        counter += 1
    count.append(counter)

longest = max(count)

for i in range(len(count)):
    if count[i] == longest:
        print(names[i])


