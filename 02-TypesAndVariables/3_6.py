import math

h = input("Your height [m]: ")
h = int(h)
d = 3.57 * math.sqrt(h)

print("From seaside: ", d)

hotel = d + 20
print("From tower: ", hotel)