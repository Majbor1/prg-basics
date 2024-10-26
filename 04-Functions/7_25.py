def f(text):
    last = 0
    result = ""
    for char in text:
        if last == len(text)-1:
            result += char
        else:
            result += char + '-'
        last += 1
    return result

print(f("Marcin"))
print(f(""))
print(f("E"))
print(f("UE"))