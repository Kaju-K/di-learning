while True:
    try:
        number = int(input("Insert a number: "))
        break
    except:
        print("It should be a number. Try again.")


if (number%2 == 0):
    print("Your number is even.")
else:
    print("Your number is odd.")