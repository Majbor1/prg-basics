class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
        return self.fare

    def print_recepit(self):
        print(f"Distance: {self.distance}, rate: {self.rate_per_km}, fare: {self.calculate_fare(self.distance)}")
        


def main():
    ride1 = TaxiRide(2)
    ride2 = TaxiRide(2)
    ride1.distance = 20
    ride2.distance = 100
    ride1.print_recepit()
    ride2.print_recepit()


if __name__ == "__main__":
    main()
