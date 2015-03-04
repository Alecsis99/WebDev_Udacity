import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello Udacity! This is cool!')
        self.response.write('See if the files are updated in Google')
application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
