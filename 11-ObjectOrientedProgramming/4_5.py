from termo import Termometer
import random
import math

def main():
    rand_temp = round(random.uniform(34.0, 42.0), 1)

    my_term = Termometer(rand_temp)

    my_term.on()
    my_term.display_temp()
    my_term.off()
    my_term.display_temp()

if __name__ == "__main__":
    main() 