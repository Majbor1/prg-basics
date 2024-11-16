arr1 = [2, 3, 2, 5, 8, 1, 9, 8]
unique = []

for i in range(len(arr1)):
    is_unique = True
    for j in range(len(arr1)):
        if i != j and arr1[i] == arr1[j]:
            is_unique = False
            break

    if is_unique:
        unique.append(arr1[i])
    
print(*unique)