# Exercise 1

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    pass

if __name__ == "__main__":
    all_cats = [Bengal("Cat One", 5), Chartreux("Cat Two", 2), Siamese("Cat Three", 8)]

    sara_pets = Pets(all_cats)

    sara_pets.walk()

# Exercise 2

class Dog:
    def __init__(self, name, age, weight) -> None:
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"
    
    def run_speed(self):
        return (self.weight/self.age*10)
    
    def fight(self, other_dog):
        if round(self.run_speed()*self.weight) > round(other_dog.run_speed()*other_dog.weight):
            return f"{self.name} is victorious. ALL HAIL {self.name.upper()}"
        elif round(self.run_speed()*self.weight) < round(other_dog.run_speed()*other_dog.weight):
            return f"{self.name} is victorious. ALL HAIL {self.name.upper()}"
        else:
            return f"Both dogs killed each other in this fight. It was a tie."
        
if __name__ == "__main__":
    dog1 = Dog("Dog One", 10, 40)
    dog2 = Dog("Dog Two", 5, 35)
    dog3 = Dog("Dog Three", 900/245, 30)

    print(dog1.fight(dog2))
    print(dog2.fight(dog3))