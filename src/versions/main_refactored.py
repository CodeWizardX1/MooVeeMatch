from data.movie_data import movies_by_mood



def display_welcome_banner():
    print(
        """
        ******************************************
        ******************************************
        ******************************************
        *                                        *
        *        Welcome to MooVeeMatch!         *
        *                                        *
        ******************************************
        ******************************************
        ******************************************
        """
    )

def prompt_user_input(prompt_message):
    """prompt the user with a custom message and return their input"""
    return input(prompt_message).strip().lower() #the strip method is used to strip unintentional whitespaces from the input mood letters

def find_matching_moods(input_mood_letters):
    """search for mood matching the user's input letters using basic linear search"""
    matching_moods = [mood for mood in movies_by_mood if mood.startswith(input_mood_letters)]
    return  matching_moods

def display_movies_for_mood(mood):
    """display movies for the chosen mood"""
    print(f"\nMovies that match the mood '{mood}':")
    for movie in sorted(movies_by_mood[mood]):
        print('-----------------------------')
        print(f'Title: {movie[0]} \nRelease Year: {movie[1]} \nLogline: {movie[2]}')
    print() #print new line for readability

def handle_user_choices():
    """Main logic for prompting user and displaying recommendations"""
    while True:
        mood_letters = prompt_user_input(
            "What kind of mood are you in? (e.g., uplifting, dark, funny, romantic). "
            "\nType the beginning letter(s) of that mood and press enter: "
        )

        matching_moods = find_matching_moods(mood_letters)

        if not matching_moods:
            print("\nHmm... there aren't any moods that match those letters in our database. Try again.")
            continue #skip the rest of the code in the current iteration of the while loop and start from the top!

        #If multiple moods are found, prompt user to chose one.
        if len(matching_moods) > 1:
            print(f"\nWith those beginning letters your choices are: {', '.join(matching_moods)}") #in lieu of printing list of moods it joins them in a string separate by comma
            chosen_mood = prompt_user_input("Which mood would you like to explore? ").lower()
            if chosen_mood not in matching_moods:
                print("Invalid mood selection. Please try again.")
                continue

        else:
            chosen_mood = matching_moods[0]
            print(f"\nThe only matching mood is '{chosen_mood}'.")

        #confirm is the user wants to proceed with the chosen mood
        user_confirmation = prompt_user_input(f"Do you want to look at {chosen_mood} movies? (y/n): ")

        if user_confirmation != 'y':
            continue


        #display movies for chosen mood
        display_movies_for_mood(chosen_mood)

        continue_program = prompt_user_input("Do you want to look at other movies? (y/n): ")
        if continue_program == 'n':
            print('BYE!')
            break


#Entry point
if __name__ == "__main__":
    display_welcome_banner()
    handle_user_choices()