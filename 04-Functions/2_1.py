###
# Program for testing built-in functions
#

max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

letter = input("Enter letter: ")
print("Letter form keybord: ", letter)

number = "20303"
number = int(number)
print(number)

decimal = 304
binary = bin(decimal)
print(f"Decimal: {decimal} -> binadry: {binary}")

hex = hex(decimal)
print(f"Decimal: {decimal} -> hexadecimal: {hex}")

sign = '€'
asci = ascii(sign)
print(f"€-> assci: {asci}")

value = -17
absolute = abs(value)
print(f"Absolute value of {value} is {absolute}")