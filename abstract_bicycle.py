"""
This module contains an abstract base class (ABC) representing a bicycle.

The AbstractBicycle class defines the common attributes and methods that a bicycle should have.
It provides the blueprint for derived classes to implement their specific functionality.
"""
from abc import ABC, abstractmethod


class AbstractBicycle(ABC):
    """An abstract base class representing a bicycle."""

    def __init__(self, type_of_bicycle="None", brand="None", max_speed=0, current_speed=0):
        """Initializes an AbstractBicycle object."""
        self._type_of_bicycle = type_of_bicycle
        self._brand = brand
        self._max_speed = max_speed
        self._current_speed = current_speed
        self._the_best_qualities = set()

    def __iter__(self):
        return iter(self._the_best_qualities)

    @abstractmethod
    def get_max_distance(self):
        """
        Calculates and return the maximum distance the bicycle can travel.
        This method must be implemented by the derived classes.
        """
    @property
    def the_best_qualities(self):
        return self._the_best_qualities

    @property
    def brand(self):
        """Get the brand of the bicycle."""
        return self._brand

    @property
    def type_of_bicycle(self):
        """Get the type of the bicycle."""
        return self._type_of_bicycle

    @property
    def max_speed(self):
        """  Get the maximum speed of the bicycle.  """
        return self._max_speed

    @property
    def current_speed(self):
        """ Get the current speed of the bicycle. """
        return self._current_speed

    def __str__(self):
        """print objects by the specified pattern"""
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
               A dictionary containing the attributes and
               their corresponding values that have the specified data type.
        """
        return {key: value for key, value in obj.__dict__.items() if isinstance(value, data_type)}
