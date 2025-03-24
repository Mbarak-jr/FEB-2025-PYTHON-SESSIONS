class Vehicle:
    def move(self):
        pass  # Placeholder for polymorphism


class Car(Vehicle):
    def move(self):
        return "Driving 🚗"


class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"


class Boat(Vehicle):
    def move(self):
        return "Sailing 🚢"


# Creating objects
vehicles = [Car(), Plane(), Boat()]

# Demonstrating polymorphism
for v in vehicles:
    print(v.move())  # Each class calls its own move() method
