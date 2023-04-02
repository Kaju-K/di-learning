class Farm:
    def __init__(self, name) -> None:
        self.name = name
        self.animals = {}

    def add_animal(self, animal, amount=1):
        animal = animal.capitalize()
        if (animal in self.animals):
            self.animals[animal] += amount
        else:
            self.animals[animal] = amount

    def get_info(self):
        animals_list = ""
        for animal in self.animals:
            animals_list += f"{animal}: {self.animals[animal]}\n"
        return (

f"""{self.name}'s farm

{animals_list}
    E-I-E-I-O
"""
        )
    
    def get_animal_types(self):
        return sorted(self.animals.keys())
    
    def get_short_info(self):
        return f"{self.name}'s farm has {'s, '.join(self.get_animal_types())}s"

macdonald = Farm("McDonald")
macdonald.add_animal("cow", 5)
macdonald.add_animal("shEEp")
macdonald.add_animal("sheep")
macdonald.add_animal("goat", 12)


print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())
    