def transpose_matrix(m):
    rows, cols = len(m), len(m[0])
    
    transposed = []
    for _ in range(cols):
        transposed.append([0] * rows)
    
    # Przepisanie elementów
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = m[i][j]
    
    return transposed
    
def printing(m):
    arr = transpose_matrix(m)
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()

arr1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

arr2 = [
    [1,2,3,4,5],
    [6,7,8,9,0]
]

arr3 = [
    [5,6,7,8]
]

printing(arr1)
print()
printing(arr2)
print()
printing(arr3)