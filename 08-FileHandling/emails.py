import re

def email_sender(email_content):
    match = re.search(r"From:.*<([\w\.-]+@[\w\.-]+)>", email_content)
    return match.group(1) if match else None

def email_recipient(email_content):
    match = re.search(r"To:.*<([\w\.-]+@[\w\.-]+)>", email_content)
    return match.group(1) if match else None

def email_subject(email_content):
    match = re.search(r"Subject: (.+)", email_content)
    return match.group(1).strip() if match else None

def email_body(email_content):
    match = re.split(r"\r?\n\r?\n", email_content, maxsplit=1)
    return match[1].strip() if len(match) > 1 else None
