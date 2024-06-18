from game.player import Player
from game.ui import display_question, display_scores, get_player_answer
from utils.bible_data import load_questions
import random

class BibleTriviaGame:
    def __init__(self, num_players):
        self.players = [Player(i) for i in range(1, num_players + 1)]
        self.questions = load_questions()
        self.current_round = 0

    def start(self):
        while True:
            self.current_round += 1
            print(f"\n=== Round {self.current_round} ===\n")
            random.shuffle(self.players)
            for player in self.players:
                question = random.choice(self.questions)
                display_question(question)
                answer = get_player_answer()

                if answer == question['answer'].lower():
                    player.add_score(10)  # Adjust score based on correct answer
                    print(f"Correct! Player {player.player_id} gets 10 points.")
                else:
                    player.deduct_score(5)  # Penalty for incorrect answer
                    print(f"Incorrect! Player {player.player_id} loses 5 points.")
                
                display_scores(self.players)

            if self.current_round >= 3:  # Example: end game after 3 rounds
                break

        self.end_game()

    def end_game(self):
        print("\n=== Game Over ===\n")
        # Determine and display winner(s) based on scores
        max_score = max(player.score for player in self.players)
        winners = [player.player_id for player in self.players if player.score == max_score]
        if len(winners) == 1:
            print(f"Player {winners[0]} wins with {max_score} points!")
        else:
            print(f"We have a tie between players {', '.join(map(str, winners))} with {max_score} points each!")

        print("Thanks for playing!")

