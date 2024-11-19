with open("powers.txt", 'w') as file:
    for i in range(1, 101):
        powers = f"{i}, {i**2}, {i**3} \n"
        file.write(powers)

