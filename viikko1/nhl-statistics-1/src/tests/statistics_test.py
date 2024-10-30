import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )


    def test_search_player(self):
        player = self.stats.search("Kurri")
        self.assertAlmostEqual(player.name, "Kurri")
    
    def test_search_no_player(self):
        player = self.stats.search("Makinen")
        self.assertIsNone(player)
    
    def test_team(self):
        team = self.stats.team("EDM")
        self.assertEqual(len(team), 3)
        self.assertTrue(all(player.team == "EDM" for player in team))
    
    def test_top(self):
        top = self.stats.top(3)
        self.assertEqual(len(top), 3)
        self.assertEqual(top[0].name, "Gretzky")
        self.assertEqual(top[1].name, "Lemieux")
        self.assertEqual(top[2].name, "Yzerman")
    
    def test_top_points(self):
        top = self.stats.top(3, SortBy.POINTS)
        self.assertEqual(top[0].name, "Gretzky")
        self.assertEqual(top[1].name, "Lemieux")
        self.assertEqual(top[2].name, "Yzerman")

    def test_top_goals(self):
        top = self.stats.top(3, SortBy.GOALS)
        self.assertEqual(top[0].name, "Lemieux")
        self.assertEqual(top[1].name, "Yzerman")
        self.assertEqual(top[2].name, "Kurri")

    def test_top_assists(self):
        top = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual(top[0].name, "Gretzky")
        self.assertEqual(top[1].name, "Yzerman")
        self.assertEqual(top[2].name, "Lemieux")

    