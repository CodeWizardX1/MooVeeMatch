"""
The central script where the program runs. It prompts the user for input and calls functions from other modules to handle logic.
"""
from data.movie_data import movies_by_mood

# print(sorted(movies_by_mood["uplifting"]))#test

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

user_mood = input('What kind of mood are you in? (e.g., uplifting, dark, funny, romantic). ' + '\nType the beginning letter(s) of that mood and press enter to see if it’s here: ').lower()



def recommend_movies(input_mood):
    matching_moods_list = []
    for mood in movies_by_mood.keys():
        match_count = 0
        for idx in range(len(mood)):
            for char in range(len(input_mood)):
                if input_mood[char] == mood[char + idx]:
                    match_count += 1
                else:
                    break
            break

        if match_count == len(input_mood):
                matching_moods_list.append(mood)
    return matching_moods_list




mood_options = recommend_movies(user_mood)
user_choice = None

while user_choice is None:
    if len(mood_options) < 1:
        user_mood = input("Hmm... there aren't any moods that begin with those letters in our database. Please try again. Enter the beginning letters of your mood:  ")
        mood_options = recommend_movies(user_mood)
    elif len(mood_options) > 1:
        user_mood = input(f"With those beginning letters, your choices are {recommend_movies(user_mood)}" + "\n\nSo, what kind of mood are you in?" + "\nType the beginning letter(s) of that mood and press enter to see if it’s here: ").lower()
        mood_options = recommend_movies(user_mood)
    else:
        user_choice = input(f"The only option with those beginning letters is {mood_options[0]}. Do you want to look at {mood_options[0]} movies? Enter 'y' for yes or 'n' for no: ")