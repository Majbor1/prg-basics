###
# Takes a number from the user and counts down to zero.
#
# Modify the program so that the last five seconds of the counter
# are displayed in words, i.e. five, four, three, two, one.
#
import time

countdown = int(input("Enter the number of seconds to count down: "))

while countdown > 0:
    if countdown > 5:
        print(countdown)
        countdown -= 1
        time.sleep(1)
    elif countdown == 5:
        print("FIVE")
        countdown -= 1
        time.sleep(1)
    elif countdown == 4:
        print("FOUR")
        countdown -= 1
        time.sleep(1)
    elif countdown == 3:
        print("THREE")
        countdown -= 1
        time.sleep(1)
    elif countdown == 2:
        print("TWO")
        countdown -= 1
        time.sleep(1)
    elif countdown == 1:
        print("ONE")
        countdown -= 1
        time.sleep(1)

print("Time's up!")
