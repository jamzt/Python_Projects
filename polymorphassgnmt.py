#Parent class Planets
class Planets:
    def __init__ (self, name, composition, location, age):
        self.name = name
        self.composition = composition
        self.location = location
        self.age = age

    def planet_info(self):
            print("{self.name} is a {self.composition} planet in the {self.location}. It is {self.age} million years old.").format(self.name)


#child class Mars
class Mars(Planets):
    def __init__(self, name, composition, location, age, distance, temperature):
        super().__init__(name, composition, location, age)
        self.distance = distance
        self.temperature = temperature

    def planet_info(self):
        print("{self.name} is a {self.composition} planet in the {self.location}. It is {self.age} million years old. It's {self.distance} away from our planet and has an average temperature of {self.temperature} Celsius.")

# child class Venus  
class Venus(Planets):
    def __init__(self, name, composition, location, age, length_day, length_year):
        super().__init__(name, composition, location, age)
        self.length_day = length_day
        self.length_year = length_year

    def planet_info(self):
        print("{self.name} is a {self.composition} planet in the {self.location}. It is {self.age} million years old. One day on Venus lasts {self.length_day} and a year lasts {self.length_year}.")
        


mars = Mars("Mars", "rocky", "Solar System", "4.5 million", "140 million miles", "-60")
venus = Venus("Venus", "rocky", "Solar System", "4.5 million", "243 days", "225 days")

mars.planet_info()
venus.planet_info()