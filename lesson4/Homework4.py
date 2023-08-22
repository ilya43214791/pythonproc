team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 17, "number": 12},
]


def show_players(players: list[dict]):
    print(players)


def add_player(num: int, name: str, age: int):
    new_players = {num: 29, name: "ilya", age: "21"}
    add = team.append(new_players)


def remove_player(players: list[dict], num: int):
    for player in players:
        if player["number"] == num:
            team.remove(player)
            print("You delite player")


def main():
    show_players(team)

    add_player(num=17, name="Cris", age=31)
    add_player(num=17, name="Bob", age=39)
    remove_player(players=team, num=17)

    show_players(team)


if __name__ == "__main__":
    main()
else:
    raise SystemExit("This module in only for running")
