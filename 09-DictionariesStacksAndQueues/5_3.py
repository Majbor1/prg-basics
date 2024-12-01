translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}

word = input("Word to translate: ")

for key, value in translations.items():
    if word in translations:
        if word == key:
            print("In polish: ", value)
            break     
    else:
        print("Translate unavailable")  
        break