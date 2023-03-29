def counting_letters(sentence, character):
    return sentence.count(character)

print("Insert a sentence:")
sentence = input()

character = input("What letter do you want to count the occurance in this sentence: ")

print(counting_letters(sentence, character))