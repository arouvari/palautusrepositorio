class Player:
    def __init__(self, data):
        self.name = data.get("name")
        self.team = data.get("team")
        self.goals = data.get("goals", 0)
        self.assists = data.get("assists", 0)
        self.nationality = data.get("nationality")


    def __str__(self):
        return f"{self.name:20} {self.team}  {self.goals} + {self.assists} = {self.points}"

    @property
    def points(self):
        return self.goals + self.assists
