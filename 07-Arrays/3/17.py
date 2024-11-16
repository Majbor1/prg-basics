tuple = (50,20,40,50,30,50)

def f(tuple):
    for i in range(len(tuple)):
        count = 0
        for j in range(len(tuple)):
            if tuple[i] == tuple[j]:
                count += 1
            else:
                count += 0
        print(f"{tuple[i]}: {count}")

f(tuple)