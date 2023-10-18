from typing import List
from character_film import CharacterFilm
import json

character_film_list: List[CharacterFilm] = []

file = open('StarWars.json')
data = json.load(file)

for obj in data:
    character_film = CharacterFilm(
        obj['fields']['edited'],
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
    print(character.name)

# Luke Skywalker 6 Star Wars: Episode IV – A New Hope no
# Chewbacca 7 Star Wars Episode III: Revenge of the Sith yes
# Anakin Skywalker 7 Star Wars Episode I: The Phantom Menace no
