arr = [[-38, 19], [5,40],[-7,11],[29,16]]
arr2 = []
for i in arr:
    for j in i:
        arr2.append(j)

largest = max(arr2)
smallest = min(arr2)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == smallest:
            print(f"Smallest: {smallest} in {i+1} row and {j+1} column")
        if arr[i][j] == largest:
            print(f"Smallest: {largest} in {i+1} row and {j+1} column")