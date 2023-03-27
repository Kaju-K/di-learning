# Challange 1

number = int(input("Give me a number: "))
length = int(input("Give me a length: "))

final_list = []

for i in range(length):
    final_list.append(number*(i+1))

print(final_list)

# Challenge 2

print("Write a word and I'll cut all the duplicates that are next to each other")
word = input()

word_letters = []

for index, letter in enumerate(word):
    try:
        if (word[index] == word[index+1]):
            continue
        else:
            word_letters.append(letter)
    except:
        word_letters.append(letter)

fixed_word = "".join(word_letters)

print(fixed_word)