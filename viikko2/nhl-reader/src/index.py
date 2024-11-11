from rich.console import Console
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats

console = Console()

def main():
    seasons = [
        "2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"
    ]

    console.print("Select season", style="bold magenta")
    for i, season in enumerate(seasons, 1):
        console.print(f"[{i}] {season}")
    season_choice = int(console.input("Enter the number of the season: ")) - 1
    selected_season = seasons[season_choice]
    url = f"https://studies.cs.helsinki.fi/nhlstats/{selected_season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    while True:
        nationalities = ["FIN", "SWE", "CAN", "USA", "RUS", "SVK", "CZE", "GER", "AUT", "SUI", "DEN", "NOR", "LAT", "BLR", "SLO", "GBR"]
        console.print("Select nationality", style="bold magenta")
        for i, nat in enumerate(nationalities, 1):
            console.print(f"[{i}] {nat}")

        nationality_input = console.input("Enter the number of the nationality: ")
        nationality_choice = int(nationality_input) - 1
        selected_nationality = nationalities[nationality_choice]
        players = stats.top_scorers_by_nationality(selected_nationality)
        console.print(f"\nTop scorers of {selected_nationality} season {selected_season}\n", style="bold cyan")

        table = Table(title="Player Stats")
        table.add_column("Name", style="cyan", no_wrap=True)
        table.add_column("Team", style="magenta")
        table.add_column("Goals", justify="right", style="green")
        table.add_column("Assists", justify="right", style="green")
        table.add_column("Points", justify="right", style="green")

        for player in players:
            table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))

        console.print(table)

if __name__ == "__main__":
    main()
