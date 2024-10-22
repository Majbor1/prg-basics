###
# Functions to read any data type from the keyboard
#
def input_string(message):
    message = input(message)
    return message

def input_integer(message):
    intiger = input(message)
    return intiger

def input_real(message):
    real = input(message)
    return real

def input_boolean(message):
    boolean = input(message)
    if boolean == 'y' or boolean == 'Y':
        return True
    elif boolean == 'n' or boolean == 'N':
        return False

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print("a")
