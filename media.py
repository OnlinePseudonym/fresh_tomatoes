import webbrowser

class Video():
    """ This class provies a way to store video related information and actors
    as a parent to Movie and TvShow"""
    def __init__(self, title, summary, reviews, program_image):
        ## Initializes an instance of Video with self, the title, a summary of the plot, a link to reviews, and a picture of the box art as inputs.
        self.title = title
        self.summary = summary
        self.reviews = reviews
        self.program_image = program_image

class Movie(Video):
    """ This class provides a way to store movie related information and acts as
    a child taking title, summary, reviews, and the box art from Video"""

    def __init__(self, title, summary, reviews, program_image, duration,
                 movie_trailer_youtube):
        ## Initializes an instance of Movie with self, the title, a summary of the plot, a link to reviews, a picture of the box art, the duration of the movie, and a link to a youtube trailer as inputs.
        Video.__init__(self, title, summary, reviews, program_image)
        ## Passes attributes from Video into movie
        self.duration = duration
        self.trailer_youtube_url = movie_trailer_youtube

    def show_trailer(self):
        ## Opens a youtube video playing a trailer for the movie
        webbrowser.open(self.trailer_youtube_url)

#class TvShow(Video):
#    """ This class provieds a way to store television related information and
#    acts as a child taking title, summary, reviews, and the box art from Video"""
#    def __init__(self, title, summary, reviews, program_image, seasons, tv_station, local_listing_url):
#        ## Initializes an instance of Movie with self, the title, a summary of the plot, a link to reviews, a picture of the box art, the #duration of the movie, and a link to a youtube trailer as inputs.
#        Video.__init__(self, title, summary, program_image)
#        self.season = season
#        self.tv_station = tv_station
#        self.local_listing = local_listing_url

#    def get_local_listing(self):
#        ## Opens a website with upcoming show times of the tv show
#        webbrowser.open(self.local_listing_url)
