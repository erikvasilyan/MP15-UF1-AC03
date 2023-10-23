class Character:
    _edited = None
    _name = None
    _created = None
    _gender = None
    _skin_color = None
    _hair_color = None
    _eye_color = None
    _mass = None
    _homeworld = None
    _birth_year = None

    def __init__(self, edited, name, created, gender, skin_color, hair_color, height, eye_color, mass,
                homeworld, birth_year):
        self._edited = edited
        self._name = name
        self._created = created
        self._gender = gender
        self._skin_color = skin_color
        self._hair_color = hair_color
        self._height = height
        self._eye_color = eye_color
        self._mass = mass
        self._homeworld = homeworld
        self._birth_year = birth_year

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, new_gender):
        self._gender = new_gender

    @property
    def homeworld(self):
        return self._homeworld

    @homeworld.setter
    def homeworld(self, new_homeworld):
        self._homeworld = new_homeworld

    @property
    def birth_year(self):
        return self._birth_year

    @birth_year.setter
    def birth_year(self, new_birth_year):
        self._birth_year = new_birth_year
