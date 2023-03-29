# Exercise 1

def display_message():
    print("I'm learning python")

display_message()

# Exercise 2

def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book("Alice in Wonderland")

# Exercise 3

def describe_city(city, country="Earth"):
    if (country == "Earth"):
        print(f"{city} is a city that stays on Earth")
    else:
        print(f"{city} is in {country}")

describe_city("Rio de Janeiro", "Brazil")

# Exercise 4

import random

def random_guess(num):
    random_number = random.randint(1,100)
    if (num == random_number):
        print("Wow! You got it right, you are a lucky person")
    else:
        print(f"Too bad, the number was {random_number}")

random_guess(3)

# Exercise 5

def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}")

make_shirt()
make_shirt("medium")
make_shirt("small", text="I Love Corn")

# Exercise 6

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(names):
    printed_names = '\n'.join(names)
    print(f"{printed_names}")

def make_great(names):
    for index, name in enumerate(names):
        names[index] = f"The Great {name}"
    
make_great(magician_names)

show_magicians(magician_names)

# Exercise 7

import random

def get_random_temp(season):
    season = season.lower()
    if (season == "winter"):
        return random.uniform(-10,16)
    if (season == "spring"):
        return random.uniform(0,23)
    if (season == "summer"):
        return random.uniform(-23,40)
    if (season == "autumn"):
        return random.uniform(0,23)
        

def main(season):
    temp = get_random_temp(season)
    if (temp <= 0):
        print(f"Brrr, it's freezing! Wear some extra layers today. It's {temp:.2f} degrees Celsius")
    elif (0 < temp <= 16):
        print(f"Quite chilly! Don't forget your coat. It's {temp:.2f} degrees Celsius")
    elif (16 < temp <= 23):
        print(f"A little bit cold, nothing to worry about, maybe one coat will be fine. It's {temp:.2f} degrees Celsius")
    elif (23 < temp <= 32):
        print(f"It's fine, go have fun. It's {temp:.2f} degrees Celsius")
    else:
        print(f"Well, it's hot outside, don't forget to drink water. It's {temp:.2f} degrees Celsius")

main("winter")