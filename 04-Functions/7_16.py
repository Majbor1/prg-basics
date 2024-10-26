def f(palindrom):
    back = palindrom[::-1]
    if back == palindrom:
        return True
    else:
        return False

print(f("radar"))
print(f("12-11-21"))
print(f("book"))