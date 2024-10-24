from in_range_checker import is_in_range

number = int(input("A number: "))
x = 2
y = 15

print(f"Number {number} in the range <{x},{y}>: {is_in_range(x, y, number)}")