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


def put_to_html(select_data):
    with open("animals_template.html", "r", encoding="utf-8") as fd:
        html_str = fd.read()
    if "__REPLACE_ANIMALS_INFO__" in html_str:
        html_str = html_str.replace("__REPLACE_ANIMALS_INFO__", select_data)
        with open("animals_template.html", "w", encoding="utf-8") as fd:
            fd.write(html_str)


def get_filtered_animals_data(animals_data):
    select_data = ""
    select_data += '<ul class="cards">'
    for fox in animals_data:
        select_data += '<li class="cards__item">\n'
        if 'name' in fox:
            select_data += f'<div class="card__title">{fox["name"]}</div>\n'
        select_data += '<p class="card__text">\n'
        if 'characteristics' in fox and 'diet' in fox['characteristics']:
            select_data += f"<strong>Diet: </strong>"
            select_data += f"{fox['characteristics']['diet']}<br/>\n"
        if 'locations' in fox and len(fox['locations']) > 0:
            select_data += f"<strong>Location: </strong>"
            select_data += f"{fox['locations'][0]}<br/>\n"
        if 'characteristics' in fox and 'type' in fox['characteristics']:
            select_data += f"<strong>Type: </strong>"
            select_data += f"{fox['characteristics']['type']}<br/>\n"
        select_data += '</p></li>\n'
    select_data += '</ul>'
    return select_data.strip()


def main():
    animals_data = load_data('animals_data.json')
    select_data = get_filtered_animals_data(animals_data)
    put_to_html(select_data)


if __name__ == "__main__":
    main()
