class PlayerStats:
    def __init__(self, player_reader):
        self.players = player_reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        filtered_players = filter(lambda player: player.nationality == nationality, self.players)
        return sorted(filtered_players, key=lambda player: player.points, reverse=True)
