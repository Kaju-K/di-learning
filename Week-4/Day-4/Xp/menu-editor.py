from exercise import MenuItem
import os
import time

def load_manager():
    pass

def menu_display():
    print("     Menu")
    print("(a) Add an item")
    print("(d) Delete an item")
    print("(v) View the menu")
    print("(x) Exit")
    print()

def show_user_menu():
    invalid_input = False
    os.system("cls")
    while True:
        if invalid_input:
            print(f"{option} is not a valid input, try again")
        menu_display()
        option = input().lower()
        if (option == "a"):
            invalid_input = False
            add_item_to_menu()
        elif (option == "d"):
            invalid_input = False
            remove_item_from_menu()
        elif (option == "v"):
            invalid_input = False
            show_restaurant_menu()
        elif (option == "x"):
            os.system("cls")
            invalid_input = False
            show_restaurant_menu()
            break
        else:
            invalid_input = True

def add_item_to_menu():
    time.sleep(0.2)
    os.system("cls")
    while True:
        name = input("What's the name of the dish you want to add (if you want to go back, type 'back'): ").title()
        if name == "Back":
            return
        try:
            price = int(input(f"\nType the price of {name} (if you want to change the name, type any text): "))
            dish = MenuItem(name, price)
            if dish.save():
                print(f"\n{name} was successfully added in the Menu with the price of {price}")
                return name, price
            else:
                print(f"\nSorry, {name} it's already on the Menu")
            break
        except:
            continue

def remove_item_from_menu():
        time.sleep(0.2)
        os.system("cls")
        name = input("What's the name of the dish you want to remove (if you want to go back, type 'back'): ").title()
        if name == "Back":
                return
        if MenuItem.get_by_name(name):
            MenuItem.delete_from_menu(name)
            print(f"{name} deleted")
        else:
            print(f"{name} is not on the menu")

def show_restaurant_menu():
    time.sleep(0.2)
    os.system("cls")
    menu = MenuItem.all()
    for dishes in menu:
        print(f"{dishes[1]} {'-'*5} {dishes[2]} NIS")
    print()

show_user_menu()
