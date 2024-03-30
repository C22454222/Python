class vehicles(object):

    def __init__(self, modelYear, miles, VIN, engine, transmission, options=None):
        self.model = modelYear
        self.miles = miles
        self.VIN = VIN
        self.engine = engine
        self.transmission = transmission
        self.options = options or []

    def __str__(self):
        print(f"Model year : {self.model}")
        print(f"Mileage: {self.miles}")
        print(f"VIN: {self.VIN}")
        print(f"Engine: {self.engine}")
        print(f"Transmission {self.transmission}")
        print(f"Options: {' ,'.join(self.options)}")
        print()



class car(vehicles):
    def __init__(self, modelYear, miles, VIN, engine, transmission, options, numDoors = 2):
        super().__init__(modelYear, miles, VIN, engine, transmission, options)
        self.numDoors = numDoors

    def __str__(self):
        super().__str__()
        print(f"Number of doors: {self.numDoors}")
        print()


class truck(vehicles):
    def __init__(self, modelYear, miles, VIN, engine, transmission, options, wheels = 18):
        super().__init__(modelYear, miles, VIN, engine, transmission, options)
        self.wheels = wheels

    
    def __str__(self):
        super().__str__()
        print(f"Number of wheels: {self.wheels}")
        print()



class SUV(vehicles):
    def __init__(self, modelYear, miles, VIN, engine, transmission, options, capacity = 5):
        super().__init__(modelYear, miles, VIN, engine, transmission, options)
        self.capacity = capacity


    def __str__(self):
        super().__str__()
        print(f"Capacity: {self.capacity}")
        print()


class minivan(vehicles):
    def __init__(self, modelYear, miles, VIN, engine, transmission, options, seats = 5):
        super().__init__(modelYear, miles, VIN, engine, transmission, options)
        self.seats = seats

    def __str__(self):
        super().__str__()
        print(f"Capacity: {self.seats}")
        print()

# Instantiate examples for testing
car_example = car(2020, 30000, '123ABC', 'V6', 'Automatic', ['Leather Seats', 'Navigation'],4)
truck_example = truck(2018, 50000, '456DEF', 'V8', 'Manual', ['Towing Package', 'Bed Liner'], 20)
suv_example = SUV(2022, 15000, '789GHI', '4-Cylinder', 'Automatic', ['Sunroof', 'Third Row Seating'], 7)
minivan_example = minivan(2019, 40000, '101JKL', 'V6', 'Automatic', ['DVD Player', 'Power Sliding Doors'], 10)

# Display information for testing
car_example.__str__()
truck_example.__str__()
suv_example.__str__()
minivan_example.__str__()
