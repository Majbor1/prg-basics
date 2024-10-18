attemps = 0
user_pin = 5555

while attemps < 3:
    pin = int(input("Enter pin: "))
    if pin != user_pin:
        print("Incorrect...")
        attemps += 1
    else:
        print("Correct!")
        break
if attemps == 3:
    print("Sorry, your payment card has been blocked")