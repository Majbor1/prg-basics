import math
size_tree = int(input("Enter tree circumference in cm: "))
cut_down = size_tree / math.pi >= 50

print(f"Tree can be cut down: {cut_down}")