facebook = True
twitter = True
instagram = False
accout = 0

if facebook:
    accout += 1
if twitter:
    accout += 1
if instagram:
    accout += 1

if accout >= 2:
    print("You are a good influencer")
else:
    print("You aren't good infuencer")