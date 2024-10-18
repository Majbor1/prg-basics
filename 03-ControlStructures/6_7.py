age = int(input("Enter your age: "))
age_group = ""

if age < 13:
    age_group = "Child"
elif age <= 19:
    age_group = "Teen"
elif age <= 64:
    age_group = "Adult"
elif age < 64:
    age_group = "Senior"

print(f"Your age group: {age_group}")