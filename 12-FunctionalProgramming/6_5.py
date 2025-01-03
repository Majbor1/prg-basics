numbers = []

for i in range(1, 21):
    numbers.append(i)

result = list(filter(lambda x: x%6 == 0, numbers))
print(*result)