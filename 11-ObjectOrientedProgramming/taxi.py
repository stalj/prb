class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
        return self.fare
    def print_receipt(self):
        print("poxuy")



def main():
    # your program
    tax1=TaxiRide(23)
    tax2=TaxiRide(34)
    print(f'first  {tax1.calculate_fare(45)}')
    print(f'second {tax2.calculate_fare(25)}')
    

if __name__ == "__main__":
    main()
