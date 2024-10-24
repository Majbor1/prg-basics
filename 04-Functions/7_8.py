def f(number, even):
    number = str(number)
    is_even = 0
    is_odd = 0
    if even:
        for i in number:
            i = int(i)
            if i % 2 == 0:
                is_even += i
        return is_even
    else: 
        for i in number:
            i = int(i)
            if i % 2 != 0:
                is_odd += i
        return is_odd
    
print(f(3124,True))
print(f(3124,False))
print(f(20576,False))
print(f(20576,True))
print(f(13115,True))
    