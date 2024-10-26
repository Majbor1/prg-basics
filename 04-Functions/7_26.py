def f(code):
    i = 0
    control = 0
    sum = 0
    for char in code:
        char = int(char)
        if i < 3:
            sum += char
            i += 1 
        else: 
            control += char
    
    if sum % 7 == control:
        return True
    else:
        return False
    
print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))

