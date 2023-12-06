#hna we'll store all the dictionaries and stuff, like les noms de salles w les creneaux w dakchi

class room ():
    def __init__(self, type, ID, name, emploi, materiaux, places):
        self.type = type
        self.ID = ID
        self.name = name
        self.emploi = emploi
        self.materiaux = materiaux
        self.places = places
