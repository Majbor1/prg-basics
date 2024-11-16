arr1 = [
    ["water","book","sky"],
    [True,False],
    [5,3,1],
    [3,2,1]
]

arr2 = [
    ["water","book","sky"],
    [True,False,True],
    [5,3,1],
    [3,2]
]

def f(array1, array2):
    if len(array1) == len(array2):
        for i in range(len(array1)):
            if array1[i] != array2[i]:
                return False
        return True
    else: 
        return False
    
def printing(array1, array2):
    print(f"Array 1: {array1}")
    print(f"Array 2: {array2}")
    result = ""
    if f:
        result = "Comparison: arrays are the same"
    else:
        result = "Comparison: arrays are not the same"
    
    print(result)



for i in range(len(arr1)):
    printing(arr1[i], arr2[i])
    print()