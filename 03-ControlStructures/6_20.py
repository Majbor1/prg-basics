decimal = int(input("Enter a decimal number: "))

reminder = decimal % 2
quotient = decimal // 2

while reminder == 0:
    reminder = quotient % 2
    quotient = decimal // 2
    

