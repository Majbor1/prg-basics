###
# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#
total_washing_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ')
extra_rinse = input('Extra rinse? (y/n): ')
extra_spin = input('Extra spin? (y/n): ')

if program == 'j':
    time = 20
elif program == 'u':
    time = 70
elif program == 's':
    time = 15

if extra_rinse == 'y':
    time += 15
    
if extra_spin == 'y':
    time += 9

print(f"Total washing time: {time} minutes")