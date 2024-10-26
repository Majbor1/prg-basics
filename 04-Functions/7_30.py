def power(x, n):
    result = 0
    if n == 0:
        result = 1
    else:
        result = x * power(x, n-1)
    return result

print(power(5, 3))
print(power(6, 2))
print(power(-2, 2))
print(power(0, 0))