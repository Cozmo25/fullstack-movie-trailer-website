import webbrowser

# Create a class of type movie
class Movie():
    """ This class provides a way to store movie related information"""

    #Set the properties of the class
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):

        """
        initialize instance of class Movie

        :param movie_title: string
        :param movie_storyline: string
        :param poster_image: string
        :param trailer_youtube: string
        """

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Define a function to show the movie trailer
    # when a user clicks on the movie poster on the site

        """
        Initializing instance for opening the youtube video

        :return: webbrowser to play thriller
        """
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
