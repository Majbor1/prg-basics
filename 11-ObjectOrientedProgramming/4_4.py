from e_book import Ebook

def main():
    my_ebook = Ebook("Lalka", "Bolesław Prus", 578, 128)

    my_ebook.open()
    my_ebook.show_status()
    for i in range(130):
        my_ebook.next_page()
    my_ebook.show_status()
    my_ebook.close()
    my_ebook.next_page()


if __name__ == "__main__":
    main() 