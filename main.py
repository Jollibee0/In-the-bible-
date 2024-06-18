from game.game import BibleTriviaGame

if __name__ == "__main__":
    num_players = int(input("Enter number of players: "))
    game = BibleTriviaGame(num_players)
    game.start()
  
