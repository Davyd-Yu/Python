"""
Module: electric_bicycle

This module contains the ElectricBicycle class,

which represents an electric bicycle derived from the AbstractBicycle class.
"""
from models.abstract_bicycle import AbstractBicycle


class ElectricBicycle(AbstractBicycle):
    """A class representing an electric bicycle, derived from AbstractBicycle."""

    def __init__(self, type_of_bicycle="None", brand="None", max_speed=0,
                 current_speed=0, capacity_of_battery=0,
                 energy_consumption_per_100_m=0,
                 the_best_qualities=None):
        """ Initializes an ElectricBicycle object. """
        super().__init__(type_of_bicycle, brand, max_speed, current_speed)
        self.__capacity_of_battery = capacity_of_battery
        self.__energy_consumption_per_100_m = energy_consumption_per_100_m
        self._the_best_qualities = the_best_qualities

    def get_max_distance(self):
        """Calculates and returns the maximum distance
        the electric bicycle can travel based on the battery capacity."""
        return self.__capacity_of_battery / self.__energy_consumption_per_100_m * 100

    @property
    def capacity_of_battery(self):
        """Gets the capacity of the electric bicycle's battery """
        return self.__capacity_of_battery

    @property
    def energy_consumption_per_100_m(self):
        """Gets the energy consumption of the electric bicycle per 100 meters. """
        return self.__energy_consumption_per_100_m

    def __str__(self):
        """Returns a string representation of the ElectricBicycle object."""
        return f"{super().__str__()}, " \
               f"capacity_of_battery={self.capacity_of_battery}, " \
               f"energy_consumption_per_100_m={self.energy_consumption_per_100_m}"
