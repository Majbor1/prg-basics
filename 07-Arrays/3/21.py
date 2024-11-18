arr1 = [2,3,8,4,6,8,1]
arr2 = [1,2,3,4,5,6,7,8,9]

result = False
for i in arr1:
    if i in arr2:
        result = True
        
print(result)