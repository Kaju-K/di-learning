from game import Game

def get_user_menu_choice():
    print("\nDo you want to play a new game (y), see the score (s) or quit (q)?\n")
    answer = input()
    return answer.lower()

def print_results(results):
    print(f"Match History:\nWins: {results['win']}\nLoss: {results['loss']}\nDraws: {results['draw']}")

def main():
    results = {
        "win": 0,
        "loss": 0,
        "draw": 0,
    }
    while True:
        answer = get_user_menu_choice()
        if (answer == "q"):
            break
        if (answer == "s"):
            print_results(results)
            continue
        if (answer == "y"):
            game = Game()
            result = game.play()
            if "win" in result:
                results["win"] += 1
            elif "loose" in result:
                results["loss"] += 1
            else:
                results["draw"] += 1
            continue
        print("Command not valid. Try again")


main()