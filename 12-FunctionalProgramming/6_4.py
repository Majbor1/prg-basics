numbers = []

for i in range(1, 21):
    numbers.append(i)

powers = list(map(lambda x: x*x*x, numbers))

print(*powers)