def display_question(question):
    print(f"Question: {question['question']}")

def display_scores(players):
    print("Current Scores:")
    for player in players:
        print(f"Player {player.player_id}: {player.score}")

def get_player_answer():
    answer = input("Your answer: ").strip().lower()
    return answer
  
