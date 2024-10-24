def f(detector):
    in_room = 0
    for char in detector:
        if in_room < 3:
            if char == '+':
                in_room += 1
            elif char == '-':
                in_room -= 1
        else:
            return True
    return False
    
print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))