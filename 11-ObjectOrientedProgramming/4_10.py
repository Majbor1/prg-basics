class C:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def m(self, n):
        if self.coordinates[n - 1][0] > 0 and self.coordinates[n - 1][1] > 0:
            return True
        else:
            return False

def main():
    new = C([[2, 3], [1, 8], [-6, 4], [3, -7]])
    
    print(new.m(2))  # Check the second coordinate
    print(new.m(3))  # Check the third coordinate

if __name__ == "__main__":
    main()