class Ebook:
    def __init__(self, title, author, pages, current_page):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = current_page
        self.is_open = False

    def open(self):
        self.is_open = True
    
    def close(self):
        self.is_open = False

    def next_page(self):
        if self.is_open:
            self.current_page += 1
        else:
            print("Ebook is close")
    
    def previous_page(self):
        if self.is_open:
            self.current_page -= 1
        else:
            print("Ebook is close")

    def show_status(self):
        print(f"Title: {self.title}.")
        print(f"Written by {self.author}.")
        print(f"This e-book has {self.pages} pages.")
        if self.is_open:
            print(f"I am just reading the e-book, page {self.current_page}.")
        else:
            print("The e-book is close.")
        