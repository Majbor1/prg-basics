arr = [15, 8, 31, 47, 2, 19]

avg = 0
i = 0
while i < len(arr):
    print(arr[i], end=" ")
    avg += arr[i]
    i += 1
    
print()
print(avg/i)