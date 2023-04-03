import random
from exercise import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False) -> None:
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *dogs_names):
        if dogs_names:
            dog_names_list = [dog.name for dog in dogs_names]
            print(f"Own... {', '.join(dog_names_list)} and {self.name} are all playing together")
        else:
            print(f"{self.name} is playing by himself")

    def do_a_trick(self):
        list_tricks = [
            "does a barrel roll.",
            "stands on his back legs",
            "shakes your hand",
            "plays dead",
        ]
        if self.trained:
            print(f"{self.name} {random.choice(list_tricks)}")
        else:
            print(f"{self.name} doesn't know him any tricks. Train him first.")

dog1 = PetDog("Dog One", 10, 40)
dog2 = PetDog("Dog Two", 5, 35, True)
dog3 = PetDog("Dog Three", 900/245, 30)

dog2.play(dog1, dog3)
dog2.play()
