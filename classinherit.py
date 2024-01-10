class Animals:
    # defining common attributes for all animals
    def __init__(species, size, diet):
        self.species = 'name of species'
        self.size = ' small, med, large'
        self.diet = 'carnivore, herbivore, omnivore'


class Reptiles(Animals):
    #additional but own attrbs:
    blood = 'ectothermic'
    scales = 'yes'


class Birds(Animals):
    #additional but own attrbs:
    wings = 'yes'
    skin = 'feather'
