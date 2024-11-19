import re

file_name = 'email.txt'

with open(file_name) as file:
    content = file.read()

sender = "^jan.*com$"
repicient = '^To..com>$'
email_subject = ''
email_body = ''

find_sender = re.findall(sender, content)

print(find_sender)