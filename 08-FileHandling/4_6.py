def f(file_name):
    with open(file_name, 'r') as file:
        content = file.read()

        characters = 0

        splited_lines = content.splitlines()

        for i in splited_lines:
            for j in splited_lines:
                characters += 1
        words = content.split()

        print(f"File name: {file_name}")
        print(f"Number of lines: {len(splited_lines)}")
        print(f"Number of characters: {characters}")
        print(f"Number of words: {len(words)}")
        

f("files.txt")
f("pets.txt")
f("it_company.csv")