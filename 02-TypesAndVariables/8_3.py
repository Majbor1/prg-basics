cm = 170 

# Constants for conversion
cm_to_inches = 0.393701
inches_to_feet = 12

# Convert centimeters to inches
height_inches = cm * cm_to_inches

# Calculate feet and inches
feet = height_inches // inches_to_feet
inches = height_inches % inches_to_feet

feet = int(feet)
inches = int(inches)

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')