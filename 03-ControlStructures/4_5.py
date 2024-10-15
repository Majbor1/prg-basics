###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())
    number = ord(char)
    # add one to the character's code
    new_number = number + 1
    # replace new character code with its
    # corresponding character (use chr())
    char = chr(new_number)
    # add encrypted character to encrypted text
    encrypted_text = encrypted_text + char

print(f"plain_text: {plain_text}")
print(f"encrypted_text: {encrypted_text}")