import data_fetcher


DST_HTML_FILE = 'animals.html'


def put_to_html(select_data):
    """Replace placeholder in template file with serialized data, save new
    file as DST_HTML_FILE"""
    with open("animals_template.html", "r", encoding="utf-8") as fd:
        html_str = fd.read()
    if "__REPLACE_ANIMALS_INFO__" in html_str:
        html_str = html_str.replace("__REPLACE_ANIMALS_INFO__", select_data)
        with open(DST_HTML_FILE, "w", encoding="utf-8") as fd:
            fd.write(html_str)


def serialize_animal(animal):
    """Format extracted data into list items 'cards'."""
    select_data = ''
    select_data += '<li class="cards__item">\n'
    if 'name' in animal:
        select_data += f'<div class="card__title">{animal["name"]}</div>\n'
    select_data += '<p class="card__text">\n'
    select_data += '<ul class="info_items">'
    if 'characteristics' in animal and 'diet' in animal['characteristics']:
        select_data += f'<li class="info_itm_li"><strong>Diet: </strong>'
        select_data += f"{animal['characteristics']['diet']}</li>\n"
    if 'locations' in animal and len(animal['locations']) > 0:
        select_data += f'<li class="info_itm_li"><strong>Location: </strong>'
        select_data += f"{animal['locations'][0]}</li>\n"
    if 'characteristics' in animal and 'type' in animal['characteristics']:
        select_data += f'<li class="info_itm_li"><strong>Type: </strong>'
        select_data += f"{animal['characteristics']['type']}</li>\n"
    select_data += '</ul>'
    select_data += '</p></li>\n'
    return select_data


def get_filtered_animals_data(animals_data, usr_input):
    """Concat serialized data for animals that match user input"""
    select_data = ''
    for animal in animals_data:
        if ("name" in animal and
                usr_input.lower() in animal["name"].lower()):
            select_data += serialize_animal(animal)
    if select_data == '':
        select_data = (f'<h1 style="color:red">api-ninja isn\'t aware of <br>'
                       f'&lt; {usr_input} &gt;</h1>')
    return select_data.strip()


def main():
    """Control flow"""
    usr_input = input("Enter name of animal to produce a webpage about: ")
    animals_data = data_fetcher.fetch_data(usr_input)
    select_data = get_filtered_animals_data(animals_data, usr_input)
    put_to_html(select_data)
    print(f"Webpage was successfully generated in file {DST_HTML_FILE}")


if __name__ == "__main__":
    main()
