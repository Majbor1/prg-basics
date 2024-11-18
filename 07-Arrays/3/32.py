arr = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]
print("Before: ")
for i in arr:
    for j in i:
        print(j, end=" ")
    print()

for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[0][j], arr[-1][j] = arr[-1][j], arr[0][j]

print("After: ")
for i in arr:
    for j in i:
        print(j, end=" ")
    print()