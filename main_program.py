def main():
    import helper
    import display
    print("Welcome to our gaming hub!")
    data = helper.read_player_data()
    options = helper.create_options_dict()
    user_choice = ""
    while not user_choice.upper() == "Q":
        display.display_user_menu(options)
        user_choice = helper.get_user_option(options)
        if user_choice.upper() == "A":
            display.display_player_by_ID(data)
        elif user_choice.upper() == "B":
            display.display_smallest_value(data)
        elif user_choice.upper() == "C":
            display.display_largest_value(data)
        elif user_choice.upper() == "D":
            display.display_top_scores(data)
        elif user_choice.upper() == "E":
            helper.find_players(data)
        elif user_choice.upper() == "P":
            helper.play_game(data)
        # No need for else or error print – get_user_option handles validation
if __name__ == "__main__":
    main()