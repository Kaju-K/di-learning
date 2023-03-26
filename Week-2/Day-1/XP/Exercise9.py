min_height = 145
conversion_inch_cm = 2.54

print("What's your height in the strange metric system that, for some reason, is still used in USA (inches)?")

while True:
    try:
        person_height_inch = int(input())
        break
    except:
        print("It should be a number, try again")

person_height_cm = person_height_inch*conversion_inch_cm

print("Your height is " + str(person_height_cm) + "cm")


if (person_height_cm > 145):
    print("Have fun, enjoy your ride!")
else:
    print("Hahaha you are too small! Grow a little bit")