# Parent class
class Superhero:
    def __init__(self, name, power, strength):
        self.name = name
        self._power = power  
        self.__strength = strength 

    # Method to display superhero details
    def display_info(self):
        return f"Superhero: {self.name}, Power: {self._power}, Strength: {self.__strength}"

    # Method to use power
    def use_power(self):
        return f"{self.name} uses {self._power}!"

    # Getter for private attribute (encapsulation)
    def get_strength(self):
        return self.__strength

    # Setter for private attribute (encapsulation)
    def set_strength(self, new_strength):
        if new_strength > 0:
            self.__strength = new_strength
        else:
            print("Strength must be greater than 0!")

# Child class (Inheritance)
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, strength, flight_speed):
        super().__init__(name, power, strength)
        self.flight_speed = flight_speed

    # Override the use_power method (Polymorphism)
    def use_power(self):
        return f"{self.name} flies at {self.flight_speed} mph using {self._power}!"

    # Additional method specific to FlyingSuperhero
    def fly(self):
        return f"{self.name} is soaring through the sky at {self.flight_speed} mph!"


# Parent class for vehicles
class Vehicle:
    def move(self):
        pass  # This will be overridden by child classes

# Child class: Car
class Car(Vehicle):
    def __init__(self, model):
        self.model = model

    # Override move() method
    def move(self):
        return f"The {self.model} is Driving 🚗"

# Child class: Plane
class Plane(Vehicle):
    def __init__(self, model):
        self.model = model

    # Override move() method
    def move(self):
        return f"The {self.model} is Flying ✈️"

# Main program to demonstrate both assignments
def main():
    print("=== Assignment 1: Design Your Own Class (Superhero) ===")
    
    # Create a Superhero object
    hero1 = Superhero("Iron Man", "Tech Suit", 85)
    print(hero1.display_info())
    print(hero1.use_power())
    
    # Create a FlyingSuperhero object (Inheritance)
    hero2 = FlyingSuperhero("Superman", "Super Strength", 100, 500)
    print(hero2.display_info())
    print(hero2.use_power())  # Polymorphic behavior
    print(hero2.fly())
    
    # Demonstrate encapsulation
    print(f"Superman's strength: {hero2.get_strength()}")
    hero2.set_strength(120)
    print(f"Updated strength: {hero2.get_strength()}")
    
    print("\n=== Assignment 2: Polymorphism Challenge (Vehicles) ===")
    
    # Create vehicle objects
    car = Car("Toyota Camry")
    plane = Plane("Boeing 747")
    
    # Demonstrate polymorphism
    vehicles = [car, plane]
    for vehicle in vehicles:
        print(vehicle.move())

# Run the program
if __name__ == "__main__":
    main()