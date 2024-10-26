def f(expression):
    result = 0
    current = 0
    sign = 1
    for char in expression:
        if char.isdigit():
            current = int(char)
            result += current * sign
        elif char == '+':
            sign = 1
        elif char == '-':
            sign = -1
    return result

print(f("5+3"))
print(f("3+8+1"))
print(f("2+3-4+5-0"))
