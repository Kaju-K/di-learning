import psycopg2

HOSTNAME = "localhost"
USERNAME = "postgres"
PASSWORD = "yourpassword"
DATABASE = "di-restaurant"
PORT = 5433

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE, port=PORT )

class MenuItem:
    def __init__(self, name, price) -> None:
        self.name = name.title()
        self.price = price

    def save(self):
        if MenuItem.get_by_name(self.name):
            return False
        else:
            query = f"INSERT INTO menu (name, price) \
                    VALUES \
                        ('{self.name}', {self.price})"
            with connection.cursor() as cursor:
                cursor.execute(query)
            return True

    def delete(self):
        query = f"DELETE FROM menu WHERE name = '{self.name}'"
        with connection.cursor() as cursor:
            cursor.execute(query)

    def update(self, name, price):
        query = f"UPDATE menu \
                SET name = '{name.title()}', \
                    price = {price} \
                WHERE \
                    name = '{self.name}' AND price = {self.price}"
        with connection.cursor() as cursor:
            cursor.execute(query)
        self.name = name.title()
        self.price = price

    @classmethod
    def all(cls):
        query = "SELECT * FROM menu"
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
        return results

    @classmethod
    def get_by_name(cls, name):
        query = f"SELECT * FROM menu WHERE name = '{name}'"
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
        return results
    
    @classmethod
    def delete_from_menu(cls, name):
        query = f"DELETE FROM menu WHERE name = '{name}'"
        with connection.cursor() as cursor:
            cursor.execute(query)

# item1 = MenuItem("Burger", 35)
# item2 = MenuItem("pasta", 30)

# item_name = MenuItem.get_by_name("Burger")
# print(item_name)

# item1.save()
# item1.save()
# items = MenuItem.all()
# print(items)
# item2.save()
# item1.update("Vegan Burger", 37)
# items = MenuItem.all()
# print(items)
# item2.delete()
# MenuItem.delete(name_of_dish)
# items = MenuItem.all()
# print(items)
# item_name = MenuItem.get_by_name("Pasta")
# print(item_name)