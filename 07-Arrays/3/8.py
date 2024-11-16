arr = [2, 6, 4, 9, 7]

def f(arr):
    for i in arr:
        a = 0
        print(i, ": ", end="")
        while a < i:
            print("*", end="")
            a += 1
        print()

f(arr)