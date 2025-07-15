# Description: Runs pokemon clash and returns "win" or "lose" outcomes.
import random
# Function name: read_data
# Parameters: filename(string)
# Return Value: a list of lists
# Description: A function that takes a csv file and creates a list of lists from it
def read_data(filename = "pokemons.csv"):
    file_in = open(filename,"r") # creation of file object
    pokemon_list = [] # creation of empty list
    if filename == "pokemons.csv":
        header_line = file_in.readline()
    for line in file_in:
        line = line.strip()
        line = line.split(",")
        pokemon_list.append(line)
    file_in.close()
    return pokemon_list
# Function name: pokemon_location
# Parameters: pokemon_data(list of lists)
# Return Value: poke_loc (list of lists) and location_input(string)
# Description: returns pokemon if they match the location
def pokemon_location(pokemon_data):
    poke_loc = []
    locations_list = ["cave","water","forest"]
    prompt_variable = "Please choose a location to fight: " + ", or ".join(locations_list) + ". "
    location_input = " "
    while not (location_input == "cave" or location_input == "water" or location_input == "forest") :
        location_input = input(prompt_variable).lower()
    for poke_list in pokemon_data:
        if poke_list[4] == location_input :
            poke_loc.append(poke_list)
    return poke_loc,location_input
# Function name: write_data
# Parameters: collected(list of lists), location(string)
# Return Value: none
# Description: makes a new file of pokemon collected
def write_data(collected, location):
    file_out = open(location + ".txt", "w")
    for poke_list in collected:
        # Ensure each row has exactly 5 items
        while len(poke_list) < 5:
            poke_list.append("")
        # Print a comma‑separated line into the file
        print(",".join(poke_list), file=file_out)
    file_out.close()
# Function name: allocate_team
# Parameters: location(string), boolean to decide if we are allocating the user team or not
# Return Value: list of pokemon
# Description: allocates a team of random pokemon to a player
def allocate_team(location, user = True):
    available_pokemon = read_data(location+".txt")
    if not available_pokemon:
        print(" No Pokémon found in",location,".txt. Make sure the location has available Pokémon.")
        return []
    team = []
    for i in range(3):
        found = random.choice(available_pokemon)
        if user == True:
            print("You have found a",found[1],"congratulations\n")
        team.append(found)
    return team
# Function name: battle
# Parameters: player one team, player two team
# Return Value: string(win or lose)
# Description: determines whether player one won the fight or not
def battle(team_one,team_two):
    while len(team_one) > 0 and len(team_two) > 0 :
        opponent_choice = random.choice(team_two)
        print("Your opponent has chosen",opponent_choice[1])
        if opponent_choice[3]:
            print("The pokemon is of type",opponent_choice[2],"(and)",opponent_choice[3])
        else:
            print("The pokemon is of type", opponent_choice[2])
        player_choice = choose_pokemon(team_one)
        player_one_status = clash(player_choice,opponent_choice)
        if player_one_status == "win" :
            team_two.remove(opponent_choice)
        else:
            team_one.remove(player_choice)
    if len(team_one) == 0:
        return "loss"
    else:
        return "win"
# Function name: choose_pokemon
# Parameters: player one team
# Return Value: a list
# Description: user selects a pokemon from their team
def choose_pokemon(team):
    if len(team) > 1:
        print("\nThese pokemon are currently available to you:")
        counter = 1
        for pokemon in team:
            if pokemon[3] == "" :
                print(counter,pokemon[1],"of Type:",pokemon[2])
            else:
                print(counter,pokemon[1],"of Type:",pokemon[2],"/",pokemon[3])
            counter += 1
    chosen_pokemon = 0
    while (chosen_pokemon < 1 or chosen_pokemon > len(team)) and len(team) > 1:
        print("\n*IF CONFUSED REFER BACK TO THE EFFECTIVENESS CHART AT THE TOP* ")
        chosen_pokemon = input("\nWho would you like to enter the fight(1-" + str(len(team)) + "):")
        while not (chosen_pokemon.isdigit()):
            chosen_pokemon = input("Who would you like to enter the fight(1-" + str(len(team)) + "): ")
        chosen_pokemon = int(chosen_pokemon)
    chosen_pokemon -= 1
    if len(team) > 1:
        print("You have chosen",team[chosen_pokemon][1])
    else:
        print("\nYour", team[0][1], "has to take the last stand now, will they prevail?")
    return team[chosen_pokemon]
# Function name: clash
# Parameters: player one pokemon(list), player two pokemon(list)
# Return Value: whether player one won or not
# Description: user's pokemon fights the opponent pokemon
def clash(player_pokemon,opponent_pokemon):
    type_effectiveness = {
        'Fire': ['Grass', 'Bug', 'Ice', 'Steel'],
        'Water': ['Fire', 'Rock', 'Ground'],
        'Grass': ['Water', 'Rock', 'Ground'],
        'Electric': ['Water', 'Flying'],
        'Rock': ['Fire', 'Bug', 'Flying', 'Ice'],
        'Ground': ['Fire', 'Electric', 'Poison', 'Rock', 'Steel'],
        'Ice': ['Grass', 'Ground', 'Flying', 'Dragon'],
        'Fighting': ['Normal', 'Ice', 'Rock', 'Dark', 'Steel'],
        'Poison': ['Grass', 'Fairy'],
        'Flying': ['Fighting', 'Bug', 'Grass'],
        'Bug': ['Grass', 'Psychic', 'Dark'],
        'Psychic': ['Fighting', 'Poison'],
        'Dark': ['Psychic', 'Ghost'],
        'Ghost': ['Psychic', 'Ghost'],
        'Steel': ['Ice', 'Rock', 'Fairy'],
        'Fairy': ['Fighting', 'Dragon', 'Dark'],
        'Normal': []
    }
    player_primary = player_pokemon[2]
    player_secondary = player_pokemon[3]
    opponent_primary = opponent_pokemon[2]
    opponent_secondary = opponent_pokemon[3]
    player_types = [player_primary,player_secondary]
    opponent_types = [opponent_primary,opponent_secondary]
    # helper function to help determine if the pokemon is effective
    def is_effective(player,opponent):
        if player in type_effectiveness and opponent in type_effectiveness[player] :
            return True
        else:
            return False
    # check if the player is effective against opponent
    for attack in player_types:
        if attack:
            for defence in opponent_types:
                if defence and is_effective(attack,defence):
                    print("\n\nSUPER EFFECTIVE, the opponent's",opponent_pokemon[1],"has fainted")
                    return "win"
    # check if the opponent is effective against player
    for attack in opponent_types:
        if attack:
            for defence in player_types:
                if defence and is_effective(attack, defence):
                    print("\n\nSUPER EFFECTIVE, your", player_pokemon[1], "has fainted")
                    return "loss"
    # variable to randomly determine winner if there is a stalemate (there is a 50% chance the player wins)
    winner = random.randrange(2)
    if winner == 1 :
        print("\nYour",player_pokemon[1],"defeated the enemy",opponent_pokemon[1])
        return "win"
    else:
        print("\nYour", player_pokemon[1], "has fainted and was defeated by the enemy", opponent_pokemon[1])
        return "loss"
def main() :
    print("\nWelcome to..... POKÉMON CLASH")
    print("You will face off against your opponent in a best of 3 to determine who is GREATEST TRAINER between you.")
    effectiveness_explained = (
        "In Pokémon Clash, some types are more effective against others:\n"
        "- Fire beats Grass, Bug, Ice, and Steel\n"
        "- Water beats Fire, Rock, and Ground\n"
        "- Grass beats Water, Rock, and Ground\n"
        "- Electric beats Water and Flying\n"
        "- Ground beats Fire, Electric, Poison, Rock, and Steel\n"
        "- Ice beats Grass, Ground, Flying, and Dragon\n"
        "- Fighting beats Normal, Ice, Rock, Dark, and Steel\n"
        "- Poison beats Grass and Fairy\n"
        "- Flying beats Fighting, Bug, and Grass\n"
        "- Bug beats Grass, Psychic, and Dark\n"
        "- Psychic beats Fighting and Poison\n"
        "- Dark beats Psychic and Ghost\n"
        "- Ghost beats Psychic and Ghost\n"
        "- Rock beats Fire, Bug, Flying, and Ice\n"
        "- Steel beats Ice, Rock, and Fairy\n"
        "- Fairy beats Fighting, Dragon, and Dark\n"
        "- Normal has no type it's especially strong against\n"
        "If your Pokémon's type is effective against your opponent's, you win the clash!\n"
        "However if your Pokémon's type matches your opponent's there is a chance you may win or lose, so choose wisely!"
    )
    print(effectiveness_explained)
    pokedex = read_data()
    victories = 0
    losses = 0
    round = 1
    print("\n\nYou have started your journey to build the greatest pokémon team in existence!")
    while victories < 2 and losses < 2:
        pokemon_location_return_values = pokemon_location(pokedex)
        chosen_location = pokemon_location_return_values[1]
        pokemon_in_the_area = pokemon_location_return_values[0]
        write_data(pokemon_in_the_area, chosen_location)
        print("\nYou have started your trek in the",chosen_location,"\n")
        player_team = allocate_team(chosen_location)
        opponent_team = allocate_team(chosen_location,False)
        print("Your star-studded team is ready, now let the GAME BEGIN!\n")
        player_status = battle(player_team,opponent_team)
        if player_status == "win" :
            print("CONGRATULATIONS You have won Round",round)
            victories += 1
        else :
            print("Unfortunately, you have lost Round",round)
            losses += 1
        round += 1
    if victories == 2 :
        print("Congratulations you have proven yourself to be the greatest trainer Trexonia has ever seen")
        return "win"
    else:
        print("Legends may be defined by their victories but they are built by their losses, your time will come")
        return "loss"
if __name__ == "__main__":
    main()