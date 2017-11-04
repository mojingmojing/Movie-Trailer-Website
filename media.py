# Define class Movie
# This function gives the defintion of class Movie and
# construct movie instances when this function gets called


class Movie():
    # The input of the function is movie title, movie storyline
    # poster image web link and movie trailer link. The output
    # of this function is a movie instance with features defined
    # by input variables
    def __init__(
            self, movie_title, movie_storyline,
            poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
