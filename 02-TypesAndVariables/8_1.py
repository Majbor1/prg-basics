import math

radius = int(input("Enter radius: "))

circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print(f"Values for: {radius}")
print(f"Circumference: {round(circumference, 2)}")
print(f"Area for: {round(area, 2)}")
