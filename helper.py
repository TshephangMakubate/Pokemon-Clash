# Description: Handles data reading, menu options, player search, and game control.
import pandas as pd
import gameplay
import display
# Function name: read_player_data
# Parameters: csv_file
# Return Values: csv_DataFrame
# Purpose: Read in a csv file and convert it into a DatatFrame
def read_player_data(csv_file = "players.csv"):
    csv_DataFrame = pd.read_csv(csv_file)
    return csv_DataFrame
# Function name: create_options_dict
# Parameters: textFileStr
# Return Values: options_dict
# Purpose: Read in a text file and convert it to a dictionary
def create_options_dict(textFileStr = "menu_options.txt"):
    options_dict = {}
    fileIn = open(textFileStr , "r")
    for line in fileIn :
        key = line.strip().split(":")[0]
        value = line.strip().split(":")[1]
        options_dict[key] = value
    return options_dict
# Function name: get_user_option
# Parameters: optionsDict
# Return Values: valid_option
# Purpose: gets valid option input from the user
def get_user_option(optionsDict):
    option = ""
    while not (option in optionsDict):
        option = input("Option: ").strip().upper()
    return option
# Function name: play_game
# Parameters: data (Dataframe holding players information)
# Return Values: None
# Purpose: helps decide the winner or loser
def play_game(data):
    ids_list = list(data["id"].values)
    # Get player 1 ID
    valid_id1 = False
    while not valid_id1:
        input1 = input("Choose index of player 1: ").strip()
        if input1.isdigit():
            id1 = int(input1)
            if id1 in ids_list:
                valid_id1 = True
    # Get player 2 ID
    valid_id2 = False
    while not valid_id2:
        input2 = input("Choose index of player 2: ").strip()
        if input2.isdigit():
            id2 = int(input2)
            if id2 in ids_list:
                valid_id2 = True
    result = gameplay.main()
    # Determine names for print message
    name1 = data.loc[data["id"] == id1, "name"].values[0]
    name2 = data.loc[data["id"] == id2, "name"].values[0]
    if result == "win":
        print(name1, "wins 10 points!")
        data.loc[data["id"] == id1, "previous_score"] = 10
        data.loc[data["id"] == id2, "previous_score"] = 0
        data.loc[data["id"] == id1, "game1_score"] = data.loc[data["id"] == id1, "game1_score"] + 10
    else:
        print(name2, "wins 10 points!")
        data.loc[data["id"] == id1, "previous_score"] = 0
        data.loc[data["id"] == id2, "previous_score"] = 10
        data.loc[data["id"] == id2, "game1_score"] = data.loc[data["id"] == id2, "game1_score"] + 10
# Function name: find_players
# Parameters: data (Dataframe holding players information)
# Return Values: None
# Purpose: finds if players exist with the key conditions given by the user
def find_players(data):
    search_criteria = ["name","hobby"]
    print("Find players based on the following attributes:",search_criteria)
    key = input("Enter a key: ").strip().lower()
    while not (key == "name" or key == "hobby"):
        key = input("Enter a key: ").strip().lower()
    search_phrase = input("Enter a search phrase: ").strip().lower()
    # Perform case-insensitive matching
    filtered_data = data[data[key].str.lower().str.contains(search_phrase)]
    if len(filtered_data) == 0:
        print("No player contains", search_phrase.capitalize(), "in key", key)
    else:
        print(len(filtered_data), "player(s) contain(s)", search_phrase.capitalize(), "in key", key)
        index = 0
        while index < len(filtered_data):
            player = filtered_data.iloc[index]
            import display
            display.display_player(player)
            index = index + 1