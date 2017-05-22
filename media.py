class Movie():
    """ store the information about a movie 

    Attributes:
        title: The name of the movie
        poster_image_url: The url of the image of the poster
        trailer_youtube_url: The url of trailer on youtube
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """
        Initilize Movie with title, post url, and trail url
        """        
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
