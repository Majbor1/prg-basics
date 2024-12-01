import queue

string = input("Enter sentence: ")
stack = queue.LifoQueue()

for char in string:
    stack.put(char)

while not stack.empty():
    char = stack.get()
    print(char, end="")