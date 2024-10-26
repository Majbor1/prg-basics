def sum_natural(n):
    sum = 0
    if n == 1:
        sum = 1
    elif n >= 2:
        sum = n + sum_natural(n-1)
    return sum

print(sum_natural(1))
print(sum_natural(2))
print(sum_natural(3))
print(sum_natural(4))
print(sum_natural(5))
print(sum_natural(6))