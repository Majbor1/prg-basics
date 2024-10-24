def hide(card_number):
    i = 1
    text = ""
    for char in card_number:
        if i > 2 and i <= 12:
            text += "*"
        else: 
            text += char
        i += 1
    
    return text
