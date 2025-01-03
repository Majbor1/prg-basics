grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]

grades_wo_2 = list(filter(lambda x: x>2.0, grades))

result = sum(grades_wo_2) / len(grades_wo_2)

print(f"{result:.2f}")