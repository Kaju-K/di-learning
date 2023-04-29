import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')
django.setup()

import random
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth.models import User
from faker import Faker
from rent.models import Customer, Vehicle, Rental

# Set up Faker instance
fake = Faker()

if __name__ == "__main__":

    # Get all customers and vehicles from the database
    customers = Customer.objects.all()
    vehicles = Vehicle.objects.all()

    # Create some rentals
    for i in range(30):
        # Choose a random customer and vehicle
        customer = random.choice(customers)
        vehicle = random.choice(vehicles)

        # Generate a random rental date within the last year
        rental_date = fake.date_between(start_date='-2y', end_date='today')
        
        # Generate a random return date within the next week, or leave it blank for ongoing rentals
        if random.random() > 0.5:
            return_date = rental_date + timedelta(days=random.randint(1, 30))
            if return_date > timezone.now().date():
                return_date = None
        else:
            return_date = None

        # Create the rental instance
        rental = Rental.objects.create(
            rental_date=rental_date,
            return_date=return_date,
            customer=customer,
            vehicle=vehicle,
        )