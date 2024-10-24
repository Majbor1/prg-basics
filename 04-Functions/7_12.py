def f(n):
    result = ""
    for i in range(1, n+1):
        i = str(i)
        result += i
    return result

print(f(11))
print(f(4))