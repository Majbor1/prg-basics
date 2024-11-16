arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]

for i in arr1:
    if i in arr2:
        arr1.remove(i)

print(arr1)