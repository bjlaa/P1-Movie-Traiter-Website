import webbrowser

# Movie class helps you create movie instances with different properties:
# title, story line, poster, trailer, actors...

class  Movie():
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # defines the __init__ function

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_actors):
        self.title = movie_title
        self.story_line = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.actors = movie_actors

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
