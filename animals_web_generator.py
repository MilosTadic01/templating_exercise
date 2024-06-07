import json


def load_data(file_path):
    """Deserialize a JSON file"""
    with open(file_path, "r", encoding='utf-8') as fd:
        return json.load(fd)


def put_to_html(select_data):
    """Replace placeholder in template file with serialized data, save new
    file title 'animals_populated.html'"""
    with open("animals_template.html", "r", encoding="utf-8") as fd:
        html_str = fd.read()
    if "__REPLACE_ANIMALS_INFO__" in html_str:
        html_str = html_str.replace("__REPLACE_ANIMALS_INFO__", select_data)
        with open("animals_populated.html", "w", encoding="utf-8") as fd:
            fd.write(html_str)


def serialize_animal(fox):
    """Format extracted data into list items 'cards'."""
    select_data = ''
    select_data += '<li class="cards__item">\n'
    if 'name' in fox:
        select_data += f'<div class="card__title">{fox["name"]}</div>\n'
    select_data += '<p class="card__text">\n'
    select_data += '<ul class="info_items">'
    if 'characteristics' in fox and 'diet' in fox['characteristics']:
        select_data += f'<li class="info_items_li"><strong>Diet: </strong>'
        select_data += f"{fox['characteristics']['diet']}</li>\n"
    if 'locations' in fox and len(fox['locations']) > 0:
        select_data += f'<li class="info_items_li"><strong>Location: </strong>'
        select_data += f"{fox['locations'][0]}</li>\n"
    if 'characteristics' in fox and 'type' in fox['characteristics']:
        select_data += f'<li class="info_items_li"><strong>Type: </strong>'
        select_data += f"{fox['characteristics']['type']}</li>\n"
    select_data += '</ul>'
    select_data += '</p></li>\n'
    return select_data


def get_filtered_animals_data(animals_data, skin_type):
    """Concat serialized data for animals that match user criterion"""
    select_data = ''
    for fox in animals_data:
        if ("skin_type" in fox["characteristics"] and
                fox["characteristics"]["skin_type"] == skin_type):
            select_data += serialize_animal(fox)
    return select_data.strip()


def get_user_input(animals_data):
    """Create a set for user to choose from and get their input. If an
    animal is missing the 'skin_type' key, it is not considered a candidate
    because it can not match user's criterion."""
    skin_types = set()
    for fox in animals_data:
        if "skin_type" in fox["characteristics"]:
            skin_types.add(fox["characteristics"]["skin_type"])
    print("\nWe will only include animals with the skin type of your choice.")
    print("Skin types:")
    for item in skin_types:
        print(f'- {item}')
    while True:
        skin_type = input("Enter your choice (mind the caps): ").strip()
        if skin_type in skin_types:
            break
        print("That skin type was not listed, try again.")
    return skin_type


def main():
    """Control flow"""
    animals_data = load_data('animals_data.json')
    skin_type = get_user_input(animals_data)
    select_data = get_filtered_animals_data(animals_data, skin_type)
    put_to_html(select_data)


if __name__ == "__main__":
    main()
