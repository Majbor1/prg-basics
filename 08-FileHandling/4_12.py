def fantasy(line):
    with open("books_fantasy.txt", 'a') as b_fantasy:
        b_fantasy.write(f"{line} \n")

def historical(line):
    with open("books_historical.txt", 'a') as b_historical:
        b_historical.write(f"{line} \n")

def romance(line):
    with open("books_romance.txt", 'a') as b_romance:
        b_romance.write(f"{line} \n")

def classic(line):
    with open("books_classic.txt", 'a') as b_classic:
        b_classic.write(f"{line} \n")

with open("books.csv") as o_file:
    content = o_file.read()
    
splited_lines = content.splitlines()

for line in splited_lines:
    if "Fantasy" in line:
        fantasy(line)
    elif "Historical" in line:
        historical(line)
    elif "Romance" in line:
        romance(line)
    elif "Classic" in line:
        classic(line)
    