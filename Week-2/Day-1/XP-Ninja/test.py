print("Let's play a Game!")
print("Try to write the biggest sentence without using the letter \"A\"")

game_on = True
sentence = ""

def message_continue():
    global game_on
    while True:
        print("Do you want to continue playing: (y) or (n)")
        answer = input()
        if (answer == "y"):
            break
        elif (answer == "n"):
            game_on = False
            break
        else:
            print("Type \"y\" for Yes or \"n\" for No")

while game_on:
    print(f"\nThe biggest sentence so far is: {sentence}")
    print("Insert your sentence:")
    temp_sentence = input().lower()
    if ("a" in temp_sentence):
        print("tsc tsc... I told you not to use the letter \"A\"")
        message_continue()
    elif (len(temp_sentence) < len(sentence)):
        print("tsc tsc... This is not longer than the previous sentence")
        message_continue()
    else:
        sentence = temp_sentence
        print("\nNice one!")
        message_continue()