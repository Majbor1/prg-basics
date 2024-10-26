def f(sentence):
    without = ""
    for char in sentence:
        if char == " ":
            without += ""
        else:
            without += char
    
    return without

print(f("integrated development environment"))
print(f("A programming language is a system of notation for writing computer programs"))