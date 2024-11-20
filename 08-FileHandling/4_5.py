from emails import email_sender, email_recipient, email_subject, email_body

# Load the email content
with open('email.txt') as file:
    email_content = file.read()

# Extract and print the email components
print("Sender Email Address:", email_sender(email_content))
print("Recipient Email Address:", email_recipient(email_content))
print("Email Subject:", email_subject(email_content))
print("Email Body:")
print(email_body(email_content))
