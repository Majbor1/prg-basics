from contact import Contact

class Contact_list:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, email, telephone):
        new_contact = Contact(name, email, telephone)
        self.contacts.append(new_contact)


    def display_contacts(self):
        for contact in self.contacts:
            print(contact)