import collections
import os

example = "A good book would sometimes cost as much as a good house."

class Text:
    def __init__(self, text) -> None:
        self.text = text.lower()
        self.separated_text = self.text.split(" ")
        pass

    def check_frequency(self, word):
        amount = collections.Counter(self.separated_text)[word]
        return amount if amount else None
    
    def most_common_word(self):
        most_common_word = collections.Counter(self.separated_text).most_common(1)[0][0]
        number_of_times = collections.Counter(self.separated_text).most_common(1)[0][1]
        return f"The most common word in the text is \"{most_common_word}\", appearing {number_of_times} times"
    
    def all_words(self):
        return list(set(self.separated_text))
    
    @classmethod
    def from_file(cls, text_file):
        base = os.path.dirname(__file__)

        with open(base + "/" + text_file, "r") as f:
            text = f.read()
        return text

a = Text(example)
print(a.check_frequency("good"))
print(a.most_common_word())
print(a.all_words())

text = Text.from_file("the_stranger.txt")
b = Text(text)
print(b.most_common_word())
