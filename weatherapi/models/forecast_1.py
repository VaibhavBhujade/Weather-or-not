# -*- coding: utf-8 -*-

"""
    weatherapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import weatherapi.models.forecastday_1

class Forecast1(object):

    """Implementation of the 'Forecast1' model.

    TODO: type model description here.

    Attributes:
        forecastday (list of Forecastday1): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "forecastday":'forecastday'
    }

    def __init__(self,
                 forecastday=None):
        """Constructor for the Forecast1 class"""

        # Initialize members of the class
        self.forecastday = forecastday


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        forecastday = None
        if dictionary.get('forecastday') != None:
            forecastday = list()
            for structure in dictionary.get('forecastday'):
                forecastday.append(weatherapi.models.forecastday_1.Forecastday1.from_dictionary(structure))

        # Return an object of this model
        return cls(forecastday)

