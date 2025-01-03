from functools import reduce


numbers = [2,4,6,3,7,5]

even = list(filter(lambda x: x%2 == 0, numbers))

sum_even = reduce(lambda x, y: x+y, even)
print(sum_even)