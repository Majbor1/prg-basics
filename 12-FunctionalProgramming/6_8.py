values = [37,51,44,23,78,92,39,84,83,51]

def min_pts(limit):
    return lambda pts: pts>=limit

p70 = list(filter(min_pts(70), values))
p40 = list(filter(min_pts(40), values))
p30 = list(filter(min_pts(30), values))

print("Min 70 pts: ", *p70)
print("Min 40 pts: ", *p40)
print("Min 30 pts: ", *p30)
