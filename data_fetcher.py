import requests
import os

API_KEY = os.getenv('API_KEY')
API_ENDPOINT_PREFIX = 'https://api.api-ninjas.com/v1/animals?name='


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary.
    """
    url = API_ENDPOINT_PREFIX + animal_name + '&X-Api-Key=' + API_KEY
    animals_data = requests.get(url).json()
    return animals_data
