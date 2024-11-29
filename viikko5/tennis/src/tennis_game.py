class TennisGame:
    score_print = ["Love", "Fifteen", "Thirty", "Forty"]
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.tied()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.advantage()
        else:
            return self.normal_score()

    def tied(self):
        if self.m_score1 < 3:
            return f"{self.score_print[self.m_score1]}-All"
        return "Deuce"

    def advantage(self):
        diff = self.m_score1 - self.m_score2
        if diff == 1:
            return "Advantage player1"
        if diff >= 2:
            return "Win for player1"
        if diff == -1:
            return "Advantage player2"
        return "Win for player2"

    def normal_score(self):
        return f"{self.score_print[self.m_score1]}-{self.score_print[self.m_score2]}"
