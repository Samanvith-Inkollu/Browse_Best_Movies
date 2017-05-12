import webbrowser
#This was only to check if we could open the webbrowser to play the trailer. The code will run if we omit this as well.
class Movie():
    #1. According to google style guide to python the first letter (cont.)
    #2. (cont.) while defining a class must be a capital letter.
    #3. Link - (https://google.github.io/styleguide/pyguide.html)
    def __init__(self, movie_title, imdb_rating, movie_storyline, poster_image, trailer_youtube):
        #4. self is the object that is being created.
        self.title = movie_title
        self.rating = imdb_rating
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        #5. The information to be initiliazed in our class.

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        #This was only to check if we could open the webbrowser to play the trailer. The code will run if we omit this as well.
        
        
    

