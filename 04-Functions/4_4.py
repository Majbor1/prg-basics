###
# Calculates the sum of the digits in a number
#
import math
def sum_digits(number):
    result = 0
    if number < 0:
        number = abs(number)
    number = str(number)
    for i in number:
        i = int(i)
        result += i
    return result

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')