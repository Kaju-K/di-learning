text = input("Type some text: ")

if (len(text) < 10):
    print("String not long enough")
elif (len(text) > 10):
    print("Strin too long")

print(f"The first character of your text is \"{text[0]}\" and the last is \"{text[-1]}\"")

for index, letter in enumerate(text):
    print(text[0:index+1])