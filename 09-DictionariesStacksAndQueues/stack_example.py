import queue

"""
A stack is a linear data structure that follows
the Last In, First Out (LIFO) principle.
This means the last element added to the stack
is the first one to be removed. Think of a stack
as a pile of plates — the last plate you place
on the top is the first one you'll take off.
"""

# creates a stack
cards = queue.LifoQueue()

# adds elements to the top of the stack
cards.put('King of Hearts \u2665')    
cards.put('Queen of Diamonds \u2666')  
cards.put('Jack of Spades \u2660')     
cards.put(2)
cards.put(3)
cards.put(4)
cards.put(1)
cards.put(9)
cards.put(8)

## prints number of elements of the stack
print('Number of stack elements:', cards.qsize())

i = 0
sum = 0
sum2 = 0

while not cards.empty():
    card = cards.get()
    print(card)
    if i == 0 or i == 1:
        sum += card
    else:
        if str(card).isnumeric():
            sum2 += card
    i += 1 

print(f"Sum of two last elements: {sum}")
print(f"Sum of the rest elements: {sum2}")