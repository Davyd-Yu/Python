"""
This abstract class.
"""
from abc import ABC, abstractmethod


class AbstractBicycle(ABC):
    """
    An abstract base class representing a bicycle.
    """

    def __init__(self, type_of_bicycle="None", brand="None", max_speed=0, current_speed=0):
        """
        Initialize an AbstractBicycle object.
        """
        self.__type_of_bicycle = type_of_bicycle
        self.__brand = brand
        self.__max_speed = max_speed
        self.__current_speed = current_speed
        self._the_best_qualities = set()

        def __iter__(self):
            return iter(self._the_best_qualities)

    @abstractmethod
    def get_max_distance(self):
        """
        Calculates and returns the maximum distance the bicycle can travel.
        This method must be implemented by the derived classes.
        """

    @property
    def the_best_qualities(self):
        return self._the_best_qualities

    @property
    def brand(self):
        """
        Gets the brand of the bicycle.
        """
        return self.__brand

    @property
    def type_of_bicycle(self):
        """
        Gets the type of the bicycle.
        """
        return self.__type_of_bicycle

    @property
    def max_speed(self):
        """
        Gets the maximum speed of the bicycle.
        """
        return self.__max_speed

    @property
    def current_speed(self):
        """
        Gets the current speed of the bicycle.
        """
        return self.__current_speed

    def __str__(self):
        """
        Prints objects by the specified pattern
        """
        return f"Bicycle: type={self.type_of_bicycle}, brand={self.brand}, " \
               f"maxSpeed={self.max_speed}, currentSpeed={self.current_speed}, " \
               f"the_best_quantities={self._the_best_qualities}"

    def get_attributes_by_type(obj, data_type):
        """
        Returns a dictionary of attributes from the object that have values of the specified data type.
        Args:
            obj: The object from which to extract attributes.
            data_type: The data type to filter attributes by.
        Returns:
            A dictionary containing the attributes and their corresponding values
            that have the specified data type.
        """
        return {key: value for key, value in obj.__dict__.items() if isinstance(value, data_type)}
