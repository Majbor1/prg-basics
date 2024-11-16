arr = [-15, 8, -31, 47, -2, 19]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

bubble_sort(arr)

print(arr[0])
print(arr[-1])
