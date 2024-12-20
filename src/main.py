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


def prompt_user():
    mood_letters = input('What kind of mood are you in? (e.g., uplifting, dark, funny, romantic). ' + '\nType the beginning letter(s) of that mood and press enter to see if it’s here: ').lower()
    return  mood_letters



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


def get_user_mood_choice(list_of_moods):
    user_response = None
    while user_response is None or user_response == 'n':
        if len(list_of_moods) < 1:
            user_mood = input("Hmm... there aren't any moods that begin with those letters in our database. Please try again. Enter the beginning letters of your mood:  ").lower()
            list_of_moods = recommend_moods_from_db(user_mood)
        elif len(list_of_moods) > 1:
            user_mood = input(f"With those beginning letters, your choices are {recommend_moods_from_db(mood_letters)}" + "\n\nSo, what kind of mood are you in?" + "\nType the beginning letter(s) of that mood and press enter to see if it’s here: ").lower()
            list_of_moods = recommend_moods_from_db(user_mood)
        else:
            user_response = input(f"The only option with those beginning letters is {list_of_moods[0]}. Do you want to look at {list_of_moods[0]} movies? Enter 'y' for yes or 'n' for no: ").lower()
            while user_response != 'y' and user_response != 'n':
                user_response = input(f"The only option with those beginning letters is {list_of_moods[0]}. Do you want to look at {list_of_moods[0]} movies? Enter 'y' for yes or 'n' for no: ").lower()

    return list_of_moods[0]



mood_letters = input('What kind of mood are you in? (e.g., uplifting, dark, funny, romantic). ' + '\nType the beginning letter(s) of that mood and press enter to see if it’s here: ').lower()

b = recommend_moods_from_db(mood_letters)

c = get_user_mood_choice(b)