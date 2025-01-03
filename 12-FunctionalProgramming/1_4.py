ms = int(input("Enter speed: "))

ms_to_kmh = lambda x: x*3.6

result = ms_to_kmh(ms)

print(f"{ms} m/s = {int(result)} km/h")