# Exercise 1

import func

func.adding_numbers(3,4)

# Exercise 2

import random

def random_pick(number):
    if (number > 100) or (number < 1):
        print("The number should be between 1 and 100")
    else:
        random_num = random.randint(1, 100)
        if number == random_num:
            print("WOW, you are a lucky one")
        else:
            print(f"Nah, the number was: {random_num}")

random_pick(3)

# Exercise 3

import string
import random

mixed_alphabet = string.ascii_letters

random_picks = random.sample(mixed_alphabet, 5)
random_str = "".join(random_picks)

print(random_str)

# Exercise 4

import datetime

def today():
    print(datetime.date.today())

today()

# Exercise 5

import datetime

def time_until_january():
    today = datetime.datetime.now()
    next_january = datetime.datetime(today.year + 1, 1, 1)
    
    print(f"The first of January is in {next_january - today}")

time_until_january()

# Exercise 6

import datetime

def birthdate(year, month, day):
    a = datetime.datetime(year, month, day)
    print(f"You have lived {round((datetime.datetime.now() - a).total_seconds() / 60, 2)} minutes")

birthdate(1996, 10, 2)

# Exercise 7

import holidays
import datetime

def days_until_holidays():
    il_holidays = holidays.IL()
    today = datetime.datetime.today()
    
    if (today in il_holidays):
        print("Today is a Holiday!!!")

    days_to_add = datetime.timedelta(days=1)

    while True:
        if (today+days_to_add in il_holidays):
            print(f"The next holiday will be in {days_to_add.days} days")
            break
        days_to_add += datetime.timedelta(days=1)

days_until_holidays()

# Exercise 8

def age_planet(seconds, planet = "Earth"):
    planet = planet.capitalize()
    age = seconds/31557600
    relation = {
        "Earth": 1,
        "Mercury": 0.2408467,
        "Venus": 0.61519726,
        "Mars": 1.8808158,
        "Jupiter": 11.862615,
        "Saturn": 29.447498,
        "Uranus": 84.016846,
        "Neptune": 164.79132,
    }
    age /= relation[planet]
    print(f"In {planet} you are {round(age,2)} years old")

age_planet(1000000000)

# Exercise 9

from faker import Faker

fake = Faker()

users = []

def add_fake_user():
    users.append({
        "name": fake.name(),
        "address": fake.address(),
        "language_code": f"{fake.language_name()[:2].lower()}-{fake.country_code()}"
    })

add_fake_user()
add_fake_user()
add_fake_user()
add_fake_user()
add_fake_user()
add_fake_user()

print(users)