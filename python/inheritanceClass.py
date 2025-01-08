# Base Vehicle class
class Vehicle:
    def __init__(self, brand, model, year):
        self.__serial_number = f"{brand[:2]}{year}{model[:2]}"  # Encapsulated
        self.brand = brand
        self.model = model
        self.year = year
        self.engine_status = "off"
    
    def start_engine(self):
        self.engine_status = "on"
        return f"{self.brand} {self.model}'s engine is now running"
    
    def stop_engine(self):
        self.engine_status = "off"
        return f"{self.brand} {self.model}'s engine is now off"
    
    def move(self):
        if self.engine_status == "off":
            return "Please start the engine first!"
        return "Vehicle is moving"
    
    def get_serial_number(self):
        return self.__serial_number

# Car class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors
        self.type = "Car"
    
    def move(self):
        if self.engine_status == "off":
            return "Please start the engine first!"
        return f"{self.brand} {self.model} is driving on the road 🚗"
    
    def honk(self):
        return "Beep! Beep! 📢"

# Plane class inheriting from Vehicle
class Plane(Vehicle):
    def __init__(self, brand, model, year, max_altitude):
        super().__init__(brand, model, year)
        self.max_altitude = max_altitude
        self.type = "Plane"
        self.current_altitude = 0
    
    def move(self):
        if self.engine_status == "off":
            return "Please start the engine first!"
        return f"{self.brand} {self.model} is flying through the air ✈️"
    
    def increase_altitude(self, feet):
        if self.engine_status == "off":
            return "Please start the engine first!"
        new_altitude = self.current_altitude + feet
        if new_altitude <= self.max_altitude:
            self.current_altitude = new_altitude
            return f"Climbing to {self.current_altitude} feet"
        return f"Cannot exceed maximum altitude of {self.max_altitude} feet"

# Boat class inheriting from Vehicle
class Boat(Vehicle):
    def __init__(self, brand, model, year, has_sail):
        super().__init__(brand, model, year)
        self.has_sail = has_sail
        self.type = "Boat"
    
    def move(self):
        if self.engine_status == "off":
            return "Please start the engine first!"
        return f"{self.brand} {self.model} is sailing across the water ⛵"
    
    def anchor(self):
        self.stop_engine()
        return "Anchor dropped! ⚓"

# Example usage and testing
def test_vehicles():
    # Create instances
    car = Car("Toyota", "Camry", 2024, 4)
    plane = Plane("Boeing", "747", 2023, 35000)
    boat = Boat("Yamaha", "242SE", 2024, True)
    
    # Test basic functionality
    vehicles = [car, plane, boat]
    results = []
    
    for vehicle in vehicles:
        results.append(f"\nTesting {vehicle.type}: {vehicle.brand} {vehicle.model}")
        results.append(f"Serial Number: {vehicle.get_serial_number()}")
        results.append(vehicle.start_engine())
        results.append(vehicle.move())
        
        # Test specific methods
        if isinstance(vehicle, Car):
            results.append(vehicle.honk())
        elif isinstance(vehicle, Plane):
            results.append(vehicle.increase_altitude(5000))
        elif isinstance(vehicle, Boat):
            results.append(vehicle.anchor())
            
    return "\n".join(results)

# Run the tests
print(test_vehicles())
