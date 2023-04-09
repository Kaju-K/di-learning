import random

class Cards:
    def __init__(self, value, suit) -> None:
        self.value = value
        self.suit = suit

    def __repr__(self) -> str:
        return f"{self.value} of {self.suit}"

class Deck:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self) -> None:
        self.new_deck = [Cards(value, suit) for suit in Deck.suits for value in Deck.values]
        self.cards = self.new_deck.copy()
        
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        return self.cards.pop(0)

deck = Deck()
print(deck.cards)
deck.shuffle()
print(deck.cards)
print(deck.deal())
print(deck.cards)