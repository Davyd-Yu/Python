"""
This is 7-th lab where I created class Bicycle
"""


class Bicycle:
    """
    class which creates bicycles and redacts their current speed
    """
    instance = None

    def __init__(self, type_of_bicycle='', brand='', max_speed=0, cur_speed=0):
        """
        :param type_of_bicycle: type of my bicycle
        :param brand: brand of my bicycle
        :param max_speed: max speed of my bicycle
        :param cur_speed: current speed of my bicycle
        Constructor initializes parameters
        """
        self.type_of_bicycle = type_of_bicycle
        self.brand = brand
        self.max_speed = max_speed
        self.cur_speed = cur_speed

    def __str__(self):
        """
        :return: returns converted in string object
        """
        return f"type: {self.type_of_bicycle}, brand: {self.brand}," \
               f" max_speed: {self.max_speed}, cur_speed: {self.cur_speed}"

    def accelerate(self, speed):
        """
        :param speed: seed of bicycle
        :return: returns accelerated bicycle's speed
        """
        if speed < self.max_speed:
            self.cur_speed += speed
        return self.cur_speed

    def brake(self):
        """
        :return: returns 0 as current speed
        """
        self.cur_speed = 0
        return self.cur_speed

    @staticmethod
    def get_instance():
        """
        :return: this is static method to returning None for typical bicycle
        """
        if not Bicycle.instance:
           Bicycle.instance = Bicycle("typical", "typical", 0, 0)
        return Bicycle.instance


bicycles = [Bicycle.get_instance(), Bicycle("mountain", "Marta", 45, 34), Bicycle()]

for bicycle in bicycles:
    print(bicycle)

