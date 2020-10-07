#########################################
##### Name: Zhiyuan Luo             #####
##### Uniqname: kyleluo             #####
#########################################

import requests
import webbrowser

class Media:

    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL"):
        self.title = title
        self.author = author
        self.release_year = release_year
        self.url= url
    
    def info(self):
        return self.title + " by " + self.author + " ("+ str(self.release_year) + ")"

    def length(self):
        return 0

class Song(Media):
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", album = "No Album", genre = "No Genre", track_length=0):
        super().__init__(title, author, release_year, url)
        self.album= album
        self.genre= genre
        self.track_length= track_length
    
    def info(self):
        return super().info()+" ["+self.genre+"]"

    def length(self):
        return round(self.track_length/1000) 

class Movie(Media):
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", rating= "No Rating", movie_length=0):
        super().__init__(title, author, release_year, url)
        self.rating=rating
        self.movie_length=movie_length    

    def info(self):
        return super().info()+" ["+self.rating+"]"
    
    def length(self):
        return round(self.movie_length/1000/60) 



# Other classes, functions, etc. should go here




if __name__ == "__main__":
    # your control code for Part 4 (interactive search) should go here
    pass
