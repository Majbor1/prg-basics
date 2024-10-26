def f(dice):
    num_counted = ""
    for digit in '0123456789':
        count = dice.count(digit)
        count = str(count)
        num_counted += count
        highest = max(num_counted)
    
    return highest

print(f("5233165554211"))
print(f("2133"))