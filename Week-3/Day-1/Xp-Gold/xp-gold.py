# Exercise 1

import math

class Circle:
    def __init__(self, radius=1.0) -> None:
        self.radius = radius

    def perimeter(self):
        return round(2*math.pi*self.radius, 2)
    
    def area(self):
        return round(math.pi*(self.radius)**2, 2)
    
    def definition(self):
        print("A circle is the set of all points in the plane that are a fixed distance (the radius) from a fixed point (the centre).")

circle = Circle()

print(circle.perimeter())
print(circle.area())
circle.definition()

# Exercise 2

import random

class MyList:
    def __init__(self, letters_list) -> None:
        self.letters_list = letters_list
        
    def reversed_list(self):
        return sorted(self.letters_list, reverse=True)
    
    def sorted_list(self):
        return sorted(self.letters_list)
    
    def random_list(self):
        return [random.randint(min(self.letters_list),max(self.letters_list)) for _ in range(len(self.letters_list))]

# Exercise 3

class MenuManager:
    def __init__(self, menu) -> None:
        self.menu = menu

    def dishes_names(self):
        return [dish["name"] for dish in self.menu]

    def add_item(self, name, price, spice, gluten):
        self.menu.append({
            "name": name.capitalize(),
            "price": price,
            "spice": spice.upper(),
            "gluten": gluten,
        })

    def existing_dish(self, name):
        if name.capitalize() in self.dishes_names():
            return True
        return False

    def update_item(self, name, price, spice, gluten):
        name = name.capitalize()
        if self.existing_dish(name):
            self.menu[self.dishes_names().index(name)] = {
                "name": name,
                "price": price,
                "spice": spice.upper(),
                "gluten": gluten,
            }
        else:
            print(f"There is no {name.capitalize()} in the Menu")

    def remove_item(self, name):
        name = name.capitalize()
        if self.existing_dish(name):
            self.menu.remove(self.menu[self.dishes_names().index(name)])
        else:
            print(f"You already don't have {name} in your menu")

            
list_dishes = [
    {
    "name": "Soup",
    "price": 10,
    "spice": "B",
    "gluten": False,
    },
    {
    "name": "Hamburger",
    "price": 15,
    "spice": "A",
    "gluten": True,
    },
    {
    "name": "Salad",
    "price": 18,
    "spice": "A",
    "gluten": False,
    },
    {
    "name": "French Fries",
    "price": 5,
    "spice": "C",
    "gluten": False,
    },
    {
    "name": "Beef bourguignon",
    "price": 25,
    "spice": "B",
    "gluten": True,
    },
]
