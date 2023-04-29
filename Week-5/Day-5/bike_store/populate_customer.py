import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')
django.setup()

import random
from faker import Faker
from django_countries import countries
from rent.models import Customer

fake = Faker()


def get_random_country_code():
    return random.choice(list(dict(countries).keys()))

def generate_fake_customer():
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    phone_number = fake.phone_number()
    address = fake.street_address()
    city = fake.city()
    country = get_random_country_code()
    return Customer(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone_number=phone_number,
        address=address,
        city=city,
        country=country
    )

def create_fake_customers(num_customers):
    for i in range(num_customers):
        fake_customer = generate_fake_customer()
        fake_customer.save()

if __name__ == '__main__':
    create_fake_customers(30)
