ean = input("Enter EAN-13 (13 long): ")

if len(ean) == 13:
    print("Article number is correct")
    if ean[0:3] == '590':
        print("Artice manufactured in Polnad")
else:
    print("Wrong number")