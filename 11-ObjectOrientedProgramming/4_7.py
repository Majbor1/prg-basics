class Statistics:
    def __init__(self, numbers):
        self.numbers = numbers.split()

    def add_number(self):
        next_number = input("Enter next number")
        if next_number.isnumeric:
            self.numbers.append(next_number)
        else:
            print("Entered value isn't a number")

    def display_numbers(self):
        for number in self.numbers:
            print(f"{number}", end=' ')

    def smallest(self):
        self.smallest = min(self.numbers)

    def largest(self):
        self.largest = max(self.numbers)
        
    def aritmetic(self):
        self.sum = 0
        for number in self.numbers:
            self.sum += int(number)
        self.aritmetic = self.sum / len(self.numbers)
        
    def median(self):
        self.numbers.sort()
        if len(self.numbers) % 2 != 0:
            self.median = self.numbers[(len(self.numbers)//2)+1]
        else:
            self.median = (self.numbers[len(self.numbers)//2] + self.numbers[len((self.numbers2)//2 + 1)])/2

    def display_stats(self):
        print(f"Minimum: {self.smallest}")
        print(f"Maximum: {self.largest}")
        print(f"Arithmetic mean: {self.aritmetic}")
        print(f"Median: {self.median}")


def main():
    my_stats = Statistics("12 13 6 9 17")

    my_stats.display_numbers()
    my_stats.largest()
    my_stats.smallest()
    my_stats.aritmetic()
    my_stats.median()
    my_stats.display_stats()
    

if __name__ == "__main__":
    main() 