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

a = MenuManager(list_dishes)

a.add_item("Tartar Tuna", 18, "A", False)

a.update_item("Tartar Tuna", 20, "A", False)

a.update_item("Ceviche", 16, "A", True)

a.remove_item("Tartar Tuna")

a.remove_item("Ceviche")
print(a.menu)