class Family:
    def __init__(self, members, last_name) -> None:
        self.members = members
        self.last_name = last_name

    def born(self, *name):
        for baby in name:
            print(f"Congratulations for the birth of {baby.capitalize()}")
            self.members.append({
                "name": baby.capitalize(),
                "age": 0,
                "gender": None,
                "is_child": True,
            })

    def is_18(self, name):
        existing_names = [member["name"] for member in self.members]
        if (name in existing_names):
            if (self.members[existing_names.index(name)]["age"] >= 18):
                return True
            return False
        print(f"{name} is not part of this family")

    def family_presentation(self):
        print(f"Last Name: {self.last_name}\nNames: {', '.join([member['name'] for member in self.members])}")

class TheIncredibles(Family):
    def use_power(self, name):
        name = name.capitalize()
        for member in self.members:
            if (member.name != name):
                continue
            if (member.age >= 18):
                print(f"The power of {name} is to {member.power}.")
                break
            raise Exception(f"{name} is under 18 years old, {name} cannot use any power")
        
    def born(self, *name):
        for baby in name:
            print(f"Congratulations for the birth of {baby.capitalize()}")
            self.members.append({
                "name": baby.capitalize(),
                "age": 0,
                "gender": None,
                "is_child": True,
                "power": "Unknown Power",
                "incredible_name": None,
            })
        
    def incredible_presentation(self):
        super().family_presentation()
        print(f"Incredble Names: {', '.join([member['incredible_name'] if member['incredible_name'] else 'No Incredible name yet' for member in self.members])}")
        print(f"Powers: {', '.join([member['power'] for member in self.members])}")
        pass
            



members = [
    {
    "name": "John",
    "age": 45,
    "gender": "Male",
    "is_child": False,
    },
    {
    "name": "Mary",
    "age": 42,
    "gender": "Female",
    "is_child": False,
    },
    {
    "name": "Bob",
    "age": 24,
    "gender": "Male",
    "is_child": False,
    },
    {
    "name": "Jane",
    "age": 27,
    "gender": "Female",
    "is_child": False,
    },
]

incredible_members = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly', 'incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
]

doe_family = Family(members, "Doe")

doe_family.born("Jack", "Peter")

doe_family.is_18("Christina")
doe_family.is_18("John")

doe_family.family_presentation()

incredible_family = TheIncredibles(incredible_members, "Incríveis")

incredible_family.incredible_presentation()
incredible_family.born("Baby Jack")
incredible_family.incredible_presentation()
