employee = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]

result = list(map(lambda x: x[0].upper()+", "+x[1], employee))

for name in result:
    print(name)