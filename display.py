# Description: Displays player info, menu, top scores, and min/max values.
# Function name: display_user_menu
# Parameters: optionsDict
# Return Value: None
# Description: Displays all menu options to the user.
def display_user_menu(optionsDict):
    for key in optionsDict:
        print(key, "->", optionsDict[key])
# Function name: display_player
# Parameters: data
# Return Value: None
# Description: Displays all player info from a Series object including total score.
def display_player(data):
    total = data["game1_score"] + data["game2_score"] + data["game3_score"]
    print(data["name"], "[#" + str(data["id"]) + "]")
    print("   The game 1 score is", data["game1_score"])
    print("   The game 2 score is", data["game2_score"])
    print("   The game 3 score is", data["game3_score"])
    print("   Total score is", total)
# Function name: display_smallest_value
# Parameters: data
# Return Value: None
# Description: Finds and displays the player with the smallest value for a selected key.
def display_smallest_value(data):
    keys = ["game1_score", "game2_score", "game3_score"]
    print("Select from this list:", keys)
    key = input("Enter a key: ").strip().lower()
    while not key in keys:
        key = input("Enter a key: ").strip().lower()
    smallest = data.iloc[0]
    index = 1
    while index < len(data):
        if data.iloc[index][key] < smallest[key]:
            smallest = data.iloc[index]
        index = index + 1
    display_player(smallest)
# Function name: display_largest_value
# Parameters: data
# Return Value: None
# Description: Finds and displays the player with the largest value for a selected key.
def display_largest_value(data):
    keys = ["game1_score", "game2_score", "game3_score"]
    print("Select from this list:", keys)
    key = input("Enter a key: ").strip().lower()
    while not key in keys:
        key = input("Enter a key: ").strip().lower()
    largest = data.iloc[0]
    index = 1
    while index < len(data):
        if data.iloc[index][key] > largest[key]:
            largest = data.iloc[index]
        index = index + 1
    display_player(largest)
# Function name: display_player_by_ID
# Parameters: data
# Return Value: None
# Description: Displays the player by ID if valid input is provided.
def display_player_by_ID(data):
    user_id_input = input("Enter Player ID: ")
    if user_id_input.isdigit():
        user_id = int(user_id_input)
        if user_id >= 0 and user_id <= 119:
            index = 0
            found = False
            while index < len(data):
                if data.iloc[index]["id"] == user_id:
                    display_player(data.iloc[index])
                    found = True
                    break
                index = index + 1
            if not found:
                print("Not Accepted.")
        else:
            print("Not Accepted.")
    else:
        print("Not Accepted.")
# Function name: display_top_scores
# Parameters: data
# Return Value: None
# Description: Displays the top N total scores after sorting them manually.
def display_top_scores(data):
    number_valid = False
    while not number_valid:
        number_input = input("How many top scores (max is 100) do you want to display?\nEnter a number: ")
        if number_input.isdigit():
            num = int(number_input)
            if num >= 1 and num <= 100:
                number_valid = True
    totals = []
    index = 0
    while index < len(data):
        total = data.iloc[index]["game1_score"] + data.iloc[index]["game2_score"] + data.iloc[index]["game3_score"]
        totals.append(total)
        index = index + 1
    sorted_totals = []
    while len(totals) > 0:
        max_value = totals[0]
        max_index = 0
        index = 1
        while index < len(totals):
            if totals[index] > max_value:
                max_value = totals[index]
                max_index = index
            index = index + 1
        sorted_totals.append(max_value)
        totals.pop(max_index)
    index = 0
    while index < num and index < len(sorted_totals):
        print(str(index + 1) + ".", sorted_totals[index])
        index = index + 1