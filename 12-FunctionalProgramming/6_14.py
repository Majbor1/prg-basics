values = [508,500,512,499,492,511,503,476,501,509]

intcorrect = list(filter(lambda x: abs(500-x) >= 500*0.02, values))

procentage = (len(intcorrect)/len(values))*100

print("Bottle capacity: 500 ml")
print("Filling tolerance: 2%")
print("Filled bottles: ")
print(*values, sep=", ")
print(f"Incorrect filled: {procentage:.0f}%")