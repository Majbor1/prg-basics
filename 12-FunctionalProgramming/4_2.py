recorded_values = [48,47,54,50,42,68,39,46]

too_high = list(filter(lambda v: v>50, recorded_values))

print(*too_high, sep=", ")