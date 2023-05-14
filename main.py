class Bicycle:
    instance = None

    @staticmethod
    def get_instance():
        return Bicycle.instance

    def __init__(self, type, brand, max_speed, current_speed):
        self.type = type
        self.brand = brand
        self.max_speed = max_speed
        self.current_speed = current_speed

    def accelerate(self, speed):
        if speed < self.max_speed:
            self.current_speed += speed
        return self.current_speed

    def brake(self):
        self.current_speed = 0
        return self.current_speed

    def increase_price(self, price):
        return price + 50

    def __str__(self):
        return f"type: {self.type}, brand: {self.brand}, max_speed: {self.max_speed}, current_speed: {self.current_speed}"


bicycles = [Bicycle.get_instance(), Bicycle("mountain", "Marta", 45, 34)]

for bicycle in bicycles:
    print(bicycle)
