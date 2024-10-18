dogs_age = int(input("Enter dog's age: "))
dog_to_human = 0
i = 1

while i <= dogs_age:
    if i <= 2:
        dog_to_human += 10.5 
    else:
        dog_to_human += 4
    i += 1
    
print(f"The dog's age in human years is {dog_to_human}")