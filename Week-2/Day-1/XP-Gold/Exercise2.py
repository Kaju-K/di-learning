print("Insert the number of the month and I'll tell you the season of this month:")
while True:
    try:
        month = int(input())
        break
    except:
        print("Put the number of the month, I don't accept texts. Try again.")

if (3 <= month <=5):
    print("This month is in Spring")
elif (6 <= month <= 8):
    print("This month is in Summer")
elif (9 <= month <= 11):
    print("This month is in Autumn")
elif (1 <= month <=2) or (month == 12):
    print("This month is in Winter")
else:
    print("This month doesn't exist")