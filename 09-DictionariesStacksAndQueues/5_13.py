import queue

stack = queue.LifoQueue()
experssion = "8 3 1 + / 3 2 - 4 + * ="

for char in experssion:
    result = 0
    if char in "0123456789":
        stack.put(char)
    elif char in "+-*/":
        first = stack.get()
        second = stack.get()
        first = int(first)
        second = int(second)
        if char == '+':
            result = first + second
        elif char == '-':
            result = second -first
        elif char == '*':
            result = first * second    
        elif char == '/':
            result = second / first
        stack.put(int(result))
    elif char == '=':
        result = stack.get()
        print(result)