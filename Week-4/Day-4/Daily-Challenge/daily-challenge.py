import requests
import random
import psycopg2

HOSTNAME = "localhost"
USERNAME = "postgres"
PASSWORD = "271828"
DATABASE = "di-countries"
PORT = 5433

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE, port=PORT)

url = "https://restcountries.com/v3.1/all"

def get_data(url):
    response = requests.get("https://restcountries.com/v3.1/all")
    return response.json()

def get_random_countries(data, amount):
    return random.choices(data, k=amount)

def informations(country):
    name = country['name']['common']
    try:
        capital = country['capital'][0].replace("'", "''")
    except:
        capital = None
    flag_image = country['flags']['svg']
    try:
        flag_alt = country['flags']['alt'].replace("'", "''")
    except:
        flag_alt = None
    subregion = country['subregion']
    population = country['population']
    
    return name, capital, flag_image, flag_alt, subregion, population

def string_checker(value):
    if isinstance(value, int):
        return value
    return "NULL" if (not value) else f'\'{value}\''

def insert_query(table, data):
    name, capital, flag_image, flag_alt, subregion, population = map(string_checker, data)

    query = f"INSERT INTO {table} (name, capital, flag_image, flag_alt, subregion, population) \
            VALUES \
            ({name}, {capital}, {flag_image}, {flag_alt}, {subregion}, {population}) "
    
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()

response = get_data(url)
countries = get_random_countries(response, 10)
for country in countries:
    insert_query("country", informations(country))
    print(f"{country['name']['common']} added to the table")