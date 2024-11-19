def f(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()

            characters = 0

            splited_lines = content.splitlines()

            for i in splited_lines:
                for j in splited_lines:
                    characters += 1
            words = content.split()

            print(f"Number of lines: {len(splited_lines)}")
            print(f"Number of characters: {characters}")
            print(f"Number of words: {len(words)}")
    except FileNotFoundError:
        print(f"File {file_name} doesn't exist!")
        

a = input("File name: ")
f(a)