distance = 70 
hours = 1
minutes = 23

avg_speed = lambda x, y, z: x/(y+(z/60))

result = avg_speed(distance, hours, minutes)

print(round(result, 2))