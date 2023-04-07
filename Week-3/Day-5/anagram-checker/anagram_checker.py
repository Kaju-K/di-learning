import os
base = os.path.dirname(__file__)

class AnagramChecker:
    def __init__(self) -> None:
        with open(base + "/words.txt", "r") as f:
            self.valid_words = f.read().lower().splitlines()

    def is_valid_word(self, word):
        if (word in self.valid_words):
            return True
        return False
    
    def get_anagrams(self, word):
        return list(filter(lambda x: True if ((sorted(word) == sorted(x)) and (word != x)) else False, self.valid_words))