def identity_matrix(n):
    rows = []
    for i in range(n):
        cols = []
        for j in range(n):
            if j != n-(n-i):
                cols.append(0)
            elif j == n-(n-i):
                cols.append(1)
        rows.append(cols)
    
    return rows

def printing(n):
    arr = identity_matrix(n)
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()

printing(3)
print()
printing(5)
print()
printing(8)