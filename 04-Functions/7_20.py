def f(n1, n2, n3):
    largest = min(n1, n2, n3)
    smallest = max(n1, n2, n3)
    
    return largest-smallest
        
    
print(f(7,4,9))
print(f(2,12,8))