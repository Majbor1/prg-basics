def is_binary(binary_number):
    for i in binary_number:
        if i != '0' and i != '1':
            return False
    return True