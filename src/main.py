"""
The central script where the program runs. It prompts the user for input and calls functions from other modules to handle logic.
"""
from data.movie_data import movies_by_mood

print(sorted(movies_by_mood["uplifting"]))#test