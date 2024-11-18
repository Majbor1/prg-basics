def identity_matrix(n):
    rows = []
    for i in range(n):
        cols = []
        for j in range(n):
            if j != n-1:
                cols.append(0)
            elif j == n-1:
                cols.append(1)
        rows.append(cols)
    
    return rows

print(identity_matrix(5))