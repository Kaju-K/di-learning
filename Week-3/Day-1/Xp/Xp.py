# Exercise 1

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("Puss in boots", 2023-1550)
cat2 = Cat("Tom", 2023-1940)
cat3 = Cat("Garfield", 2023-1978)


def older(*args):
    oldest_cat = None

    for cat in args:
        if (not oldest_cat):
            oldest_cat = cat
        else:
            if (cat.age > oldest_cat.age):
                oldest_cat = cat

    return oldest_cat

oldest_cat = older(cat1, cat2, cat3)

print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old")

# Exercise 2

class Dog:
    def __init__(self, name, height) -> None:
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes Woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height*2} cm")

davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

print(f"{davids_dog.name} is {davids_dog.height} cm high")

davids_dog.bark()
davids_dog.jump()

print(f"{sarahs_dog.name} is {sarahs_dog.height} cm high")

sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is taller")
else:
    print(f"{sarahs_dog.name} is taller")

# Exercise 3

class Song:
    def __init__(self, lyrics) -> None:
        self.lyrics = lyrics

    def sing_me_a_song(self):
        joined_lyrics = "\n".join(self.lyrics)
        print(f"{joined_lyrics}")

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()

# Exercise 4

class Zoo:
    def __init__(self, zoo_name) -> None:
        self.animals = []
        self.name = zoo_name
    
    def add_animal(self, new_animal):
        new_animal = new_animal.capitalize()
        if (new_animal not in self.animals):
            self.animals.append(new_animal)

    def get_animals(self):
        if (not self.animals):
            print("The zoo doesn't have any animals :c")
        elif (len(self.animals) == 1):
            print(f"The zoo only has {self.animals[0]}")
        else:
            print(f"The zoo so far has these animals: {', '.join(self.animals)}")

    def sell_animal(self, animal_sold):
        animal_sold = animal_sold.capitalize()
        if (animal_sold in self.animals):
            self.animals.remove(animal_sold)
        else:
            print(f"You cannot sell the {animal_sold}. You don't have it in your Zoo")
    
    def sort_animal(self):
        sorted_animals = sorted(self.animals)
        grouped_animals = {}

        for animal in sorted_animals:
            if (not grouped_animals):
                grouped_animals[1] = [animal]
            else:
                if (animal[0] == grouped_animals[len(grouped_animals)][0][0]):
                    grouped_animals[len(grouped_animals)].append(animal)
                else:
                    grouped_animals[len(grouped_animals)+1] = [animal]

        return grouped_animals

    def get_groups(self, group):
        grouped_animals = self.sort_animal()
        if (group in grouped_animals):
            print(f"These are the animals of group {group}: {', '.join(grouped_animals[group])}")
        else:
            print(f"There is no group {group}")


ramat_gan_safari = Zoo("Ramat Gan Safari")

ramat_gan_safari.add_animal("monkey")
ramat_gan_safari.add_animal("monkEy")
ramat_gan_safari.add_animal("Snake")
ramat_gan_safari.add_animal("Zebra")
ramat_gan_safari.add_animal("Lion")
ramat_gan_safari.add_animal("aPE")
ramat_gan_safari.add_animal("BABOON")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("cougar")
ramat_gan_safari.add_animal("EeL")
ramat_gan_safari.add_animal("EEL")
ramat_gan_safari.add_animal("eel")
ramat_gan_safari.add_animal("Emu")

ramat_gan_safari.get_animals()

ramat_gan_safari.sell_animal("Tiger")
ramat_gan_safari.sell_animal("snake")

print(ramat_gan_safari.sort_animal())

ramat_gan_safari.get_groups(9)
ramat_gan_safari.get_groups(2)