import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # TODO: make a list with at least 5 movie titles
        movieList = ["Breakfast Club", "Lost Boys", "Goonies", "Avatar", "Prometheus"]
        # TODO: randomly choose one of the movies, and return it
        chosenMovie = random.choice(movieList)
        return chosenMovie

    def get(self):
        # choose a movie by invoking our new function
        movie1 = self.getRandomMovie()
        movie2 = self.getRandomMovie()

        # build the response stringm
        content1 = "<h1>Movie of the Day</h1>"
        content1 += "<p>" + movie1 + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"
        content2 = "<h1>Tomorrow's Movie</h1>"
        content2 +="<p>" + movie2 + "</p>"

        self.response.write(content1)
        self.response.write(content2)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
