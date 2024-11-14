table = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(len(table)):
    for j in range(len(table[i])):
        if i == j:
            table[i][j] += 1
    
    
for i in range(len(table)):
    for j in range(len(table[i])):
        print(table[i][j], end=" ")
    print()