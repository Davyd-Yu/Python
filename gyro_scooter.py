"""
This is module gyro scooter.
"""
from models.abstract_bicycle import AbstractBicycle


class GyroScooter(AbstractBicycle):
    """Gyro scooter class"""

    def __init__(self, type_of_bicycle="None", brand="None", max_speed=0, current_speed=0,
                 capacity_of_battery=0, battery_voltage=0, energy_consumption_per_1_km=0):
        """
        Initializes a GyroScooter object.
        """
        super().__init__(type_of_bicycle, brand, max_speed, current_speed)
        self.__capacity_of_battery = capacity_of_battery
        self.__battery_voltage = battery_voltage
        self.__power = energy_consumption_per_1_km

    def get_max_distance(self):
        """
        Calculates and returns the maximum distance
        the gyro scooter can travel based on battery capacity and voltage.
        """
        return (self.__capacity_of_battery * self.__battery_voltage) / self.__power

    @property
    def capacity_of_battery(self):
        """
        Gets the capacity of the gyro scooter's battery.
        """
        return self.__capacity_of_battery

    @property
    def battery_voltage(self):
        """
        Get the voltage of the gyro scooter's battery.
        """
        return self.__battery_voltage

    @property
    def power(self):
        """
        Gets power of the gyro scooter.
        """

        return self.__power

    def __str__(self):
        """
        Returns a string representation of the GyroScooter object.
        """
        return f"GyroScooter: type={self.type_of_bicycle}, brand={self.brand}, " \
               f"max_speed={self.max_speed}, current_speed={self.current_speed}," \
               f"capacity_of_battery={self.capacity_of_battery}," \
               f"battery_voltage={self.battery_voltage}, " \
               f"power={self.power}"
