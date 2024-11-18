import random

def rand_elem(array):
    rand = random.randint(0, len(array))
    return array[rand]

arr = [1,2,3,4,5,6,7,8,9]

for i in range(5):
    print(rand_elem(arr))