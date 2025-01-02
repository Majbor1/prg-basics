class C:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority
    
    def password(self):
        text = f"{self.surname}{self.name[0]}{self.seniority}" 
        if self.age < 18:
            print(text)
        else:
            print(text.upper())

def main():
    new_employe = C("Anna","May",17,7)
    new_employe2 = C("George","Brown",21,4)

    new_employe.password()
    new_employe2.password()

if __name__ == "__main__":
    main()