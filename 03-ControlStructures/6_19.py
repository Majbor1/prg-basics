print("SURVEY")
first = input("Are you interested in computer science? y/n: ")
second = input("Do you like playing computer games? y/n: ")
third = input("Do you have an Instagram account? y/n: ")

if first == 'y':
    first = "Yes"
elif first == 'n':
    first = "No"

if second == 'y':
    second = "Yes"
elif second == 'n':
    second = "No"

if third == 'y':
    third = "Yes"
elif third == 'n':
    third = "No"

print("SURVEY RESULTS")   
print(f"Interested in computer science: {first}")
print(f"Playing computer games: {second}")
print(f"Has an Instagram account: {third}")