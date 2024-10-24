def f(amount_to_pay):
    five = amount_to_pay // 5
    amount_to_pay = amount_to_pay - (five * 5)
    two = amount_to_pay // 2
    amount_to_pay = amount_to_pay - (two * 2)
    one = amount_to_pay

    result = five + two + one
    return result

print(f(23))
print(f(8))
print(f(2))
print(f(0))
