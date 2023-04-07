from anagram_checker import AnagramChecker
import string

punctuation_digits = string.punctuation + string.digits

def main():
    print("Hi, I'm the Anagram Checker 3000.")
    while True:
        answer = get_user_menu_choice().lower().strip()
        if (answer == "q"):
            break
        if validation_word(answer):
            print("No punctuation or numbers allowed. Try again...")
            continue
        anagram_checker = AnagramChecker()
        if (anagram_checker.is_valid_word(answer)):
            if (anagram_checker.get_anagrams(answer)):
                print(f"The word {answer} has these anagrams: {', '.join(anagram_checker.get_anagrams(answer))}")
            else:
                print(f"I cannot find any valid word that is a anagram for {answer}. Try another one :)")
            continue
        print("I don't know what is this word. Please try another one")

def get_user_menu_choice():
    return input("\nType a word (only one) so I can check the anagrams or press (q) to quit: ")

def validation_word(word):
    if (len(word.split(" ")) > 1):
        raise ValueError("I told only one word...")
    word_set = set(word)
    characters_set = set(punctuation_digits)
    if (len(word_set.intersection(characters_set)) > 0):
        return True
    
main()