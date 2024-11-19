def conventer(arr):
    one_arr = []
    for i in arr:
        for j in i:
            one_arr.append(j)
        
    return one_arr

arr1 = [
    [2,3],
    [1,5]
]
print(*conventer(arr1))

arr2 = [
    [5,0,3,7,5],
    [9,0,9,1,2]
]
print(*conventer(arr2))

arr3 = [
    [2,1],
    [3,5],
    [7,4],
    [2,6]
]
print(*conventer(arr3))