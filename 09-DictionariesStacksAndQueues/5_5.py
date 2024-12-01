paragraph = "cat dog mouse cat rat cat mouse"
words = paragraph.split()
counter = {}

for word in words:
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1
        
for word, count in counter.items():
    print(f"{word}: {count}")