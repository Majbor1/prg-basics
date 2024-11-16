def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array 

arr1 = [8,6,4,5,1,7]
print(arr1)
bubblesort(arr1)
print(arr1)
print()
arr2 = [10,11,8,9,21,7]
print(arr2)
bubblesort(arr2)
print(arr2)
print()
arr3 = [7,8,5,4,1,6]        
print(arr3)
bubblesort(arr3)
print(arr3)
print()

