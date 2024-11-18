def f1(text):
    return len(text)

def f2(text):
    words = sorted(text, key=len, reverse=True)
    return words

def f3(text):
    text.sort()
    return text

