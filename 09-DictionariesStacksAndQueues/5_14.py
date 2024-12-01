import queue

queue = queue.Queue()


while True:
    
    new_customer = input("Enter name: ")
    if new_customer != "":
        queue.put(new_customer)
    else: 
        break

i = 0
while not queue.empty():
    i += 1
    current = queue.get()
    print(f"{current}, ticket number: {i}")