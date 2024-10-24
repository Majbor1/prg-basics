def f(n):
    text = ""
    for i in range(n):
        if i != (n-1):
            text += "*/"
        else:
            text += "*"
    
    return text

print(f(4))
print(f(1))
