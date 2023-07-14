def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ],
        },
    }


game_data = game_dict()


def get_all_players(team):
    return game_data[team]["players"]


home_players = get_all_players("home")
away_players = get_all_players("away")
all_players = home_players + away_players
print(all_players)

# Build a function, num_points_per_game() that takes in an argument of a player's name
# and returns the number of points per game for that player.


def num_points_per_game(player_name):
    for player in all_players:
        if player_name == player["name"]:
            return player["points_per_game"]


# Build a function, player_age(), that takes in an argument of a player's name and returns that player's age.


def player_age(player_name):
    for player in all_players:
        if player_name == player["name"]:
            return player["age"]


# Build a function, team_colors(), that takes in an argument of the team name and returns a list of that team's colors.


def team_colors(team_name):
    for team in game_data:
        if game_data[team]["team_name"] == team_name:
            return game_data[team]["colors"]


# Build a function, team_names(), that operates on the dictionary to return a list of the team names.


def team_names():
    team_names_list = []

    for team in game_data:
        team_names_list.append(game_data[team]["team_name"])

    return team_names_list


# Build a function, player_numbers(),
# that takes in an argument of a team name and returns a list of the jersey numbers for that team.


def player_numbers(team_name):
    jersey_numbers = []

    for team in game_data:
        if game_data[team]["team_name"] == team_name:
            for player in game_data[team]["players"]:
                jersey_numbers.append(player["number"])

    return jersey_numbers


# Build a function, player_stats(),
# that takes in an argument of a player's name and returns a dictionary of that player's stats.


def player_stats(player_name):
    for player in all_players:
        if player_name == player["name"]:
            return player


# Build a function, average_rebounds_by_shoe_brand(),
# that will calculate the average number of rebounds for players who wear a particular shoe brand.
# The function should print out a message for each brand using the following format:
# "<Brand>": average_rebounds
# The average should be printed as a float with two decimal places.


def average_rebounds_by_shoe_brand():
    # Create an empty dictionary named brand_rebounds to store the total rebounds for each shoe brand.
    brand_rebounds = {}

    # Create an empty dictionary named brand_counts to store the count of players for each shoe brand.
    brand_counts = {}

    # loop through all players
    for player in all_players:
        shoe_brand = player["shoe_brand"]
        rebound = player["rebounds_per_game"]

        # If the shoe brand exists in brand_rebounds and brand_counts dictionaries:
        # Increment the rebounds for that shoe brand in brand_rebounds by the player's rebounds.
        # Increment the count for that shoe brand in brand_counts by 1.
        if shoe_brand in brand_rebounds and shoe_brand in brand_counts:
            brand_rebounds[shoe_brand] += rebound
            brand_counts[shoe_brand] += 1
        # If the shoe brand does not exist in brand_rebounds and brand_counts dictionaries:
        # Add the shoe brand as a key to brand_rebounds with the player's rebounds as the initial value.
        # Add the shoe brand as a key to brand_counts with 1 as the initial value.
        else:
            brand_rebounds[shoe_brand] = rebound
            brand_counts[shoe_brand] = 1

    for brand in brand_rebounds:
        average_rebounds_by_brand = brand_rebounds[brand] / brand_counts[brand]
        print(f"{brand}: {average_rebounds_by_brand: .2f}")


average_rebounds_by_shoe_brand()