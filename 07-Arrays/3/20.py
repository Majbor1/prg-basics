arr = [7,9,2,4,5,6]
even = []
odd = []

for i in arr:
    if i % 2 == 0:
        even.append(i)
    elif i % 2 != 0:
        odd.append(i)

for i in range(len(arr)):
    if i < len(even):
        arr[i] = even[i]
    else:
        arr[i] = odd[i-(len(even))]

print(arr)