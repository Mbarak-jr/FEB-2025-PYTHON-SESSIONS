# Parent class
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.__battery_life = battery_life  # Private attribute (Encapsulation)

    def charge(self, amount):
        self.__battery_life += amount
        print(f"{self.model} charged to {self.__battery_life}% 🔋")

    def make_call(self, number):
        print(f"Calling {number} from {self.model} 📞")

    def get_battery_life(self):
        return f"Battery: {self.__battery_life}%"

# Child class (Inheritance)


class iPhone(Smartphone):
    def __init__(self, model, battery_life, ios_version):
        super().__init__("Apple", model, battery_life)
        self.ios_version = ios_version

    def show_details(self):
        return f"iPhone {self.model}, iOS {self.ios_version}, {self.get_battery_life()}"


# Creating objects
samsung = Smartphone("Samsung", "Galaxy S24", 80)
iphone = iPhone("15 Pro", 90, "iOS 17")

samsung.charge(10)  # Output: Galaxy S24 charged to 90% 🔋
iphone.make_call("+1234567890")  # Output: Calling +1234567890 from 15 Pro 📞
print(iphone.show_details())  # Output: iPhone 15 Pro, iOS 17, Battery: 90%
