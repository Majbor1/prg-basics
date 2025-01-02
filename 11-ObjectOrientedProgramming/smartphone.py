from contact_list import Contact_list

def main():
    contact_list = Contact_list()

    contact_list.add_contact("John Brown", "brown@onet.pl", "555234000")
    contact_list.add_contact("Anna May", "am@o2.pl", "232000199")
    contact_list.add_contact("George Small", "smallg@google.pl", "222999100")
    contact_list.add_contact("Paola Big", "bigpaola@poczta.pl", "100200300")

    contact_list.display_contacts()

if __name__ == "__main__":
    main()