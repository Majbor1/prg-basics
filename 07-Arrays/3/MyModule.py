def f1(arr):
    bubble(arr)
    return arr[-2]

def f2(arr):
    bubble(arr)
    return arr[-1] - arr[0]

def f3(arr):
    bubble(arr)
    return arr[(len(arr)//2)]

def f4(arr):
    bubble(arr)
    sal = [arr[0], arr[-1]]
    return sal

def f5(arr):
    string = ""
    for i in range(len(arr)):
        if i != len(arr)-1:
            arr[i] = str(arr[i])
            string += arr[i] + "-"
        else:
            arr[i] = str(arr[i])
            string += arr[i]
    
    return string

def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr