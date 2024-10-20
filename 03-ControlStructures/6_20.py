decimal = int(input("Enter a decimal number: "))
decimal2 = decimal
binary = ""

if decimal == 0:
    binary = '0'
else:
    while decimal > 0:
        reminder = decimal % 2
        binary = str(reminder) + binary
        decimal //= 2

print(f"{decimal2}(10) -> {binary}(2)")

