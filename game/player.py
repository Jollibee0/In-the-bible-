class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.score = 0

    def add_score(self, points):
        self.score += points

    def deduct_score(self, points):
        self.score -= points

    def reset_score(self):
        self.score = 0
      
