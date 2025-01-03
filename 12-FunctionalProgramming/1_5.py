def avg_speed(distance,hours,minutes):
    return round(float(distance/(hours+(minutes/60))), 2)

print(f"Average speed: {avg_speed(70, 1, 23)} km/h")