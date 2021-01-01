# -*- coding: utf-8 -*-

"""
    weatherapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import weatherapi.models.day
import weatherapi.models.astro

class Forecastday(object):

    """Implementation of the 'Forecastday' model.

    TODO: type model description here.

    Attributes:
        date (string): Forecast date
        date_epoch (int): Forecast date as unix time.
        day (Day): See day element
        astro (Astro): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "date":'date',
        "date_epoch":'date_epoch',
        "day":'day',
        "astro":'astro'
    }

    def __init__(self,
                 date=None,
                 date_epoch=None,
                 day=None,
                 astro=None):
        """Constructor for the Forecastday class"""

        # Initialize members of the class
        self.date = date
        self.date_epoch = date_epoch
        self.day = day
        self.astro = astro


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
        date = dictionary.get('date')
        date_epoch = dictionary.get('date_epoch')
        day = weatherapi.models.day.Day.from_dictionary(dictionary.get('day')) if dictionary.get('day') else None
        astro = weatherapi.models.astro.Astro.from_dictionary(dictionary.get('astro')) if dictionary.get('astro') else None

        # Return an object of this model
        return cls(date,
                   date_epoch,
                   day,
                   astro)

