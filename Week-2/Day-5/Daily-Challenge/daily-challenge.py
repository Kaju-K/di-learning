print("Write a list of words separeted by commas (no spaces) and we'll give you back in alphabetical order")
words = input()

words_list = words.split(",")
words_list.sort()

print("\nHere are the words sorted:")
print(",".join(words_list))