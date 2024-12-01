import queue

stack = queue.LifoQueue()

number = 18


while number > 0:
    reminder = number % 2
    number = number // 2
    stack.put(reminder)

while not stack.empty():
    result = stack.get()
    print(result, end="")