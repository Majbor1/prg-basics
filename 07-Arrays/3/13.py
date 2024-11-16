arr = [15, 38, 7, 23, 14]

def occurs(number, array):
    if number in array:
        result = f"Result: number {number} appears in the array."
    else: 
        result = f"Result: number {number} doesn't appears in the array."
    
    return result

print(occurs(23, arr))
a = int(input("Enter number: "))
print(occurs(a, arr))