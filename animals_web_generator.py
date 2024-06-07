import json


def load_data(file_path):
    """Deserializes a JSON file"""
    with open(file_path, "r", encoding='utf-8') as fd:
        return json.load(fd)


# def print_entire_animals_json(animals_data):
#     for animal in animals_data:
#         for category, contents in animal.items():
#             print(f"\n{category}")
#             if type(contents) is str:
#                 print(contents)
#             elif type(contents) is list:
#                 for list_entry in contents:
#                     print(f"\t{list_entry}")
#             elif type(contents) is dict:
#                 for quality, description in contents.items():
#                     print(f"\t{quality}: {description}")


def print_filtered_animals_data(animals_data):
    for fox in animals_data:
        if 'name' in fox:
            print(f"Name: {fox['name']}")
        if 'characteristics' in fox and 'diet' in fox['characteristics']:
            print(f"Diet: {fox['characteristics']['diet']}")
        if 'locations' in fox and len(fox['locations']) > 0:
            print(f"Location: {fox['locations'][0]}")
        if 'characteristics' in fox and 'type' in fox['characteristics']:
            print(f"Type: {fox['characteristics']['type']}")
        print()


def main():
    animals_data = load_data('animals_data.json')
    print_filtered_animals_data(animals_data)


if __name__ == "__main__":
    main()
