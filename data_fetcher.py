import requests

API_ENDPOINT_PREFIX = 'https://api.api-ninjas.com/v1/animals?name='
API_KEY = 'a9gswUa/Srd5yh8f2zAQYg==vIQHjGXVE6AOGzpV'


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
    },
    """
    url = API_ENDPOINT_PREFIX + animal_name + '&X-Api-Key=' + API_KEY
    animals_data = requests.get(url).json()
    return animals_data