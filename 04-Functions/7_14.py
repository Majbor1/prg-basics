def f(detector):
    in_room = 0
    for char in detector:
        if char == '+':
            in_room += 1
        elif char == '-':
            in_room -= 1