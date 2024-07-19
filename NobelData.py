# Author: Michael Russell
# GitHub username: Mike369
# Date: 07/18/2024
# Description: Write a class named NobelData that reads a JSON file containing data on Nobel Prizes and allows
# the user to search that data.

import json


class NobelData:
    """
    A class to read Nobel Prize data from a JSON file and search for laureates by year and category.

    Attributes:
    data (dict): A dictionary to store the JSON data.
    """

    def __init__(self):
        """
        Initializes the NobelData class by reading the 'nobels.json' file and storing its data.

        Parameters:
        None

        Returns:
        None
        """
        with open('nobels.json', 'r') as file:
            self.data = json.load(file)

    def search_nobel(self, year, category):
        """
        Searches for Nobel laureates by year and category and returns a sorted list of surnames.

        Parameters:
        year (str): The year of the Nobel prize (e.g., "1975").
        category (str): The category of the Nobel prize (e.g., "economics").

        Returns:
        List[str]: A sorted list of surnames of the laureates.
        """
        laureates = []
        for prize in self.data['prizes']:
            if prize['year'] == year and prize['category'] == category:
                if 'laureates' in prize:
                    for laureate in prize['laureates']:
                        if 'surname' in laureate:
                            laureates.append(laureate['surname'])
        return sorted(laureates)
