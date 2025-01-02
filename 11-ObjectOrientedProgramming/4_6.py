from bank import BankAccount

def main():
    my_ba = BankAccount("12 3456 5555 9090 1111 0000 7722")
    my_ba.show_status()
    my_ba.deposit(25.30)
    my_ba.show_status()
    my_ba.withdraw(31.70)
    my_ba.show_status()
    my_ba.withdraw(14)
    my_ba.show_status()
    

if __name__ == "__main__":
    main() 