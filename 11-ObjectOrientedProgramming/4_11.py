class C:
    def __init__(self, data):
        self.data = data

    def m1(self, s, n):
        self.data[s] = n
    
    def m2(self, s):
        total = 0
        for char in s:
            if char in self.data.keys():
                total += self.data[char]
        return total
    
def main():
    new = C({"A":120,"D":150,"G":90,"K":110})
    new.m1("G",130)
    print(new.m2("GD"))
    print(new.m2("KEJ"))

if __name__ == "__main__":
    main()