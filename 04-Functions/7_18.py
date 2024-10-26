def f(number):
    number = str(number)
    sum = 0
    for digit in "0123456789":
        count = number.count(digit)
        if count > 1:
            sum += int(digit) * count
    return sum

print(f(1270))
print(f(230335))
print(f(513553007))