"""
Module: gyro_scooter

This module contains the GyroScooter class,
which represents a gyro scooter derived from the AbstractBicycle class.
"""
from models.abstract_bicycle import AbstractBicycle


class GyroScooter(AbstractBicycle):
    """A class representing a gyro scooter, derived from AbstractBicycle."""

    def __init__(self, type_of_bicycle="None", brand="None", max_speed=0, current_speed=0,
                 capacity_of_battery=0, battery_voltage=0, energy_consumption_per_1_km=0, the_best_qualities=None):
        """ Initializes a GyroScooter object."""
        super().__init__(type_of_bicycle, brand, max_speed, current_speed)
        self.__capacity_of_battery = capacity_of_battery
        self.__battery_voltage = battery_voltage
        self.__energy_consumption_per_1_km = energy_consumption_per_1_km
        self._the_best_qualities = the_best_qualities

    def get_max_distance(self):
        """  Calculates and returns the maximum distance
        the gyro scooter can travel based on battery capacity and voltage."""
        return (self.__capacity_of_battery * self.__battery_voltage) / self.__energy_consumption_per_1_km * 1000

    @property
    def capacity_of_battery(self):
        """Gets the capacity of the gyro scooter's battery."""
        return self.__capacity_of_battery

    @property
    def battery_voltage(self):
        """Gets the voltage of the gyro scooter's battery."""
        return self.__battery_voltage

    @property
    def energy_consumption_per_1_km(self):
        """ Gets the energy consumption of the gyro scooter per 1 kilometer.  """

        return self.__energy_consumption_per_1_km

    def __str__(self):
        """Returns a string representation of the GyroScooter object. """
        return f"{super().__str__()}, capacity_of_battery={self.capacity_of_battery}, " \
               f"battery_voltage={self.battery_voltage}, " \
               f"energy_consumption_per_1_km={self.energy_consumption_per_1_km}"
