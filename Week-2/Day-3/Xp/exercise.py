# Exercise 1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dict = dict(zip(keys, values))

print(my_dict)

# Exercise 2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

for (name, age) in family.items():
    if (age < 3):
        price = 0
    elif (3 <= age <= 12):
        price = 10
    else:
        price = 15

    family[name] = {"age": age, "price": price}

message = ""
total = 0

for name in family:
    message += f"{name} has to pay {family[name]['price']} NIS; "
    total += family[name]["price"]

message += f"And the final price is {total} NIS"

print(message)

# Exercise 3

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": ["blue"],
        "Spain": ["red"],
        "US": ["pink", "green"]
    }
}

brand["number_stores"] = 2

brand["country_creation"] = "Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

del brand["creation_date"]

brand["international_competitors"][-1]

print(f"These are the major clothes color in the US: {', '.join(brand['major_color']['US'])}")

print(f"Length of dictionary: {len(brand)}")

for keys in brand:
    print(keys)

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

brand.update(more_on_zara)

print(f"Number os stores: {brand['number_stores']}")

# Exercise 4

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

disney_users_A = {user: index for index, user in enumerate(users)}
disney_users_B = {index: user for index, user in enumerate(users)}
disney_users_C = {user: index for index, user in enumerate(sorted(users))}

disney_with_i = {user: index for index, user in enumerate(users) if "i" in user.lower()}
disney_start_m_p = {user: index for index, user in enumerate(users) if (user.lower()[0] in ["m", "p"])}