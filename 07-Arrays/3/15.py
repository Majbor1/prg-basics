tuple = (10,20,30,40,50)
result = "Reverse order: "
for i in range(len(tuple)-1, -1, -1):
    result += f"{tuple[i]} "
    
print(result)