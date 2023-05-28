"""
This module defines the Bicycle class.
"""
import sys
from abc import ABC
from models.abstract_bicycle import AbstractBicycle


class Bicycle(AbstractBicycle, ABC):
    """
    Constructor of class
    """
    __instance = None

  #  def __init__(self, type_of_bicycle="None", brand="None", max_speed=0, current_speed=0):
   #     super().__init__(type_of_bicycle, brand, max_speed, current_speed)

    @staticmethod
    def get_instance():
        """
        Gets the singleton instance of the Bicycle class.
        """
        if Bicycle.__instance is None:
            Bicycle.__instance = Bicycle()
        return Bicycle.__instance

    def accelerate(self, speed):
        """
        Accelerates the bicycle by thу specified speed
        """
        if speed < self.__max_speed:
            self.__current_speed += speed
            return self.__current_speed
        return self.__max_speed

    def brake(self):
        """
        Stops the bicycle
        """
        self.__current_speed = 0
        return self.__current_speed

    def slow_down(self, speed):
        """
        Slows the bicycle by the specified speed
        """
        if speed <= self.__current_speed:
            self.__current_speed -= speed
            return self.__current_speed
        return self.brake()

    def __str__(self):
        """
        Prints objects by the specified pattern
        """
        return f"Bicycle: type={self.type_of_bicycle}, brand={self.brand}, " \
               f"maxSpeed={self.max_speed}, currentSpeed={self.current_speed}"

    def get_max_distance(self):
        """
        Returns the maximum distance the bicycle can travel.
        """
        return sys.maxsize
