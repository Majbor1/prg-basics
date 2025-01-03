is_even = lambda x: x % 2 == 0

n = int(input("Enter number: "))
if is_even(n):
    print(f"Number {n} is even")
else:
    print(f"Number {n} is odd")