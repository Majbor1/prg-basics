def f(expression):
    digits = '0123456789'
    result = 0
    for char in expression:
        if char in digits:
            char = int(char)
            result += char
        else:
            return False
        
    return result

print(f("53"))
