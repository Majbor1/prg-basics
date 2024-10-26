def f(password):
    x = ""
    if len(password) >= 6:
        for char in password:
            if char not in x:
                x += char
            else: 
                return False
        return True
    else:
        return False
    
print(f("ax15"))
print(f("book123"))
print(f("qwerty"))
print(f("A2water3"))
print(f(""))