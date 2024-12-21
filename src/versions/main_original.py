"""
Original version of the program before refactoring
"""
from data.movie_data import movies_by_mood




def prompt_user():
    user_input = input('What kind of mood are you in? (e.g., uplifting, dark, funny, romantic). ' + '\nType the beginning letter(s) of that mood and press enter to see if it’s here: ').lower()
    return  user_input



def recommend_moods_from_db(input_mood_letters):
    matching_moods_list = []
    for mood in movies_by_mood.keys():
        match_count = 0
        for idx in range(len(mood)):
            for char in range(len(input_mood_letters)):
                if input_mood_letters[char] == mood[char + idx]:
                    match_count += 1
                else:
                    break
            break

        if match_count == len(input_mood_letters):
                matching_moods_list.append(mood)
    return matching_moods_list



#Entry point
if __name__ == "__main__":
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
    while True:
        mood_letters = prompt_user()
        list_of_moods = recommend_moods_from_db(mood_letters)
        yes_no = ['y','n']
        user_response = ""

        while user_response != 'y':
            if len(list_of_moods) < 1:
                user_mood = input("Hmm... there aren't any moods that begin with those letters in our database. Please try again. Enter the beginning letters of your mood:  ").lower()
                list_of_moods = recommend_moods_from_db(user_mood)
            elif len(list_of_moods) > 1:
                user_mood = input(f"With those beginning letters, your choices are {recommend_moods_from_db(mood_letters)}" + "\n\nSo, what kind of mood are you in?" + "\nType the beginning letter(s) of that mood and press enter to see if it’s here: ").lower()
                list_of_moods = recommend_moods_from_db(user_mood)
            else:
              while (user_response := input(f"The only option with those beginning letters is {list_of_moods[0]}. Do you want to look at {list_of_moods[0]} movies? Enter 'y' for yes or 'n' for no: ").lower()) not in yes_no:
                  print("Invalid input. Please enter 'y' or 'n'.")

            if user_response == 'n':
                break


        if user_response == 'y':
            chosen_mood = list_of_moods[0]
            print('\nThese are the movies matching your mood:')
            for movie in sorted(movies_by_mood[chosen_mood]):
                print('-----------------------------')
                print(f'Title: {movie[0]} \nRelease Year: {movie[1]} \nLogline: {movie[2]}')


        while (continue_program := input("\nDo you want to look at other movies? Enter 'y' for yes or 'n' for no: ").lower()) not in yes_no:
            print("Invalid input. Please enter 'y' or 'n'.")

        if continue_program == 'n':
            print('BYE!')
            break

