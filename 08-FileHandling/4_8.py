import re

with open("files.txt", 'r') as file:
    content = file.read()

splited_lines = content.splitlines()
pattern = r'[.]\w{4}$'

for line in splited_lines:
    name_match = re.search(pattern, line)
    if name_match:
        print(line)
