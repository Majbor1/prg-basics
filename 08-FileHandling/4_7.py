import re

text = input("Enter any text: ")

pattern = '[aeiouy]'

number = 0
for i in text:
    vowel_match = re.match(pattern, i)
    if vowel_match:
        number += 1

print(number)