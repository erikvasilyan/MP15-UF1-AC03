from typing import List
from character_film import CharacterFilm
import json


def obj_dict(ob):
    return ob.__dict__


def export_json():
    with open('characters.json', 'w') as json_file:
        json_string = json.dumps(character_film_list, default=obj_dict)
        json_file.write(json_string)


character_film_list: List[CharacterFilm] = []

file = open('StarWars.json')
data = json.load(file)

for obj in data:
    character_film = CharacterFilm(
        obj["fields"]["edited"],
        obj['fields']['name'],
        obj['fields']['created'],
        obj['fields']['gender'],
        obj['fields']['skin_color'],
        obj['fields']['hair_color'],
        obj['fields']['height'],
        obj['fields']['eye_color'],
        obj['fields']['mass'],
        obj['fields']['homeworld'],
        obj['fields']['birth_year'],
        None,
        None,
        None
    )
    character_film_list.append(character_film)

for character in character_film_list:
    if character.name == 'Luke Skywalker':
        character.num_of_films = 6
        character.first_film = 'Star Wars: Episode IV - A New Hope'
        character.alive_at_the_end = False

    elif character.name == 'Chewbacca':
        character.num_of_films = 7
        character.first_film = 'Star Wars: Episode III - Revenge of the Sith'
        character.alive_at_the_end = True

    elif character.name == 'Anakin Skywalker':
        character.num_of_films = 7
        character.first_film = 'Star Wars: Episode I - The Phantom Menace'
        character.alive_at_the_end = False

    print(character.__str__())

export_json()
