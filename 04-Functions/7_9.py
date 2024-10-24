def f(x, y):
    number = 0
    for i in range(x, y):
        if i % 2 == 0 and i < 0:
            number += 1
    return number

print(f(-7,8))
print(f(-1,11))