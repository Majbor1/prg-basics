###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('Enter a side: ')
b = input('Enter b side: ')
c = input('Enter c side: ')
a = int(a)
b = int(b)
c = int(c)
cuboid_volume = a*b*c
cuboid_surface_area = 2*(a*b + a*c + c*b)
print(f'The volume of a cuboid with side {a}, {b}, {c} is {cuboid_volume}')
print(f'The surface area of a cuboid with side {a}, {b}, {c} is {cuboid_surface_area}')