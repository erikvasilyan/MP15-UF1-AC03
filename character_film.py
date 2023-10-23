import json

from character import Character


class CharacterFilm(Character):

    _num_of_films = None
    _first_film = None
    _alive_at_the_end = None

    def __init__(self, edited, name, created, gender, skin_color, hair_color, height, eye_color, mass, homeworld,
                 birth_year, num_of_films, first_film, alive_at_the_end):

        super().__init__(edited, name, created, gender, skin_color, hair_color, height, eye_color, mass,
                         homeworld, birth_year)

        self._num_of_films = num_of_films
        self._first_film = first_film
        self._alive_at_the_end = alive_at_the_end

    def __str__(self):
        character_info = (f"{self._name} is a {self._gender}, "
                          f"has {self._skin_color} skin, "
                          f"{self._hair_color} hair, "
                          f"and {self._eye_color} eyes. "
                          f"{self._name} has a height of {self._height}cm, "
                          f"a mass of {self._mass}kg and was born on {self._birth_year} in the world of {self._homeworld}.")

        if self._num_of_films is not None:
            character_info += f" {self._name} appeared in {self._num_of_films} films."

        if self._first_film is not None:
            character_info += f" First appearing in {self._first_film}."

        if self._alive_at_the_end is not None:
            character_info += f" Is {self._name} alive at the end? {'Yes' if self._alive_at_the_end else 'No'}."

        return character_info

    @property
    def num_of_films(self):
        return self._num_of_films

    @num_of_films.setter
    def num_of_films(self, new_num_of_films):
        self._num_of_films = new_num_of_films

    @property
    def first_film(self):
        return self._first_film

    @first_film.setter
    def first_film(self, new_first_film):
        self._first_film = new_first_film

    @property
    def alive_at_the_end(self):
        return self._alive_at_the_end

    @alive_at_the_end.setter
    def alive_at_the_end(self, new_alive_at_the_end):
        self._alive_at_the_end = new_alive_at_the_end
