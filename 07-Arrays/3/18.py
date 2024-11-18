from MyModule import f1, f2, f3, f4, f5

arr = [7,3,8,5,2]


print("Numbers: ", *arr)
print("Second largest number: ", f1(arr))
print("Difference between the largest and smallest values: ", f2(arr))
print("Median: ", f3(arr))
print("Smallest and largest number: ", f4(arr))
print("Numbers as a string: ", f5(arr))
