# coding=utf-8

"""
Module that uses the content of media.py to define class movie
"""

# Import required python files
import media
import fresh_tomatoes

# Create instances of movies to be displayed on the site
toy_story = media.Movie("Toy Story",
    "A story of a boy and his toys that come to life",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
    "A marine on an alien planet",
    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
    "http://www.youtube.com/watch?v=-9ceBgWV8io")

inception = media.Movie("Inception",
    "An exploration of the possiblity of our dreams",
    "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg", # noqa
    "https://youtu.be/OedvTIUDLzQ")

school_of_rock = media.Movie("School of Rock",
    "A music teacher that love rock music",
    "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Rataouille",
    "A rat who becomes a master chef",
    "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk")

hunger_games = media.Movie("Hunger Games",
    "A dystopian world where people fight to the death to save their countrymen",
    "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
    "https://www.youtube.com/watch?v=PbA63a7H0bo")

# Create an array of movies from the instances created above
movies = [toy_story, avatar,
          school_of_rock,
          ratatouille,
          inception,
          hunger_games]

# Pass the array to fresh_tomatoes open_movies_page function
# to render the movies in HTML in a web browser
fresh_tomatoes.open_movies_page(movies)

