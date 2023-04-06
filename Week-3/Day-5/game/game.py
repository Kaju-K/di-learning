import random

class Game:
    def __init__(self) -> None:
        self.items = {
            "r": "rock",
            "p": "paper",
            "s": "scissor",
        }

    def get_user_item(self):
        while True:
            item = input("Select (r)ock, (p)aper or (s)cissors: ")
            if item not in ["r", "p", "s"]:
                continue
            return item

    def get_computer_item(self):
        items = ["r", "p", "s"]
        return random.choice(items)

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "It's a draw!"
        if ((user_item == "r") and (computer_item == "s")) or ((user_item == "s") and (computer_item == "p")) or ((user_item == "p") and (computer_item == "r")):
            return "You win!"
        return "You loose!"

    def play(self):
        users_item = self.get_user_item()
        computers_item = self.get_computer_item()
        result = self.get_game_result(users_item, computers_item)
        print(f"You chose: {self.items[users_item]}. The computer chose: {self.items[computers_item]}. {result}")
        return result