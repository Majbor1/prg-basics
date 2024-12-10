class Phone():
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def Call_Friend(self, friend):
        print(f"Calling to {friend}")

    def Text_Friend(self, friend):
        print(f"Texting to {friend}")

    def Play_a_game(self):
        print("Playing Snake")

    def display(self):
        print(f"Spec: {self.brand}, {self.model}, price: {self.price}$")

def main():
    phone1 = Phone("Apple","Iphone 12 Pro Max",5600)
    phone1.Call_Friend("Oliwia")
    phone1.Play_a_game()
    phone1.Text_Friend("Kacper")
    phone1.display()

if __name__ == "__main__":
    main()