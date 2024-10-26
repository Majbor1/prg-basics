def f(name):
    acronym = ""
    words = name.split(" ")
    for word in words:
        for char in word:
            acronym += char
            break
    return acronym

print(f("Ala ma kota"))