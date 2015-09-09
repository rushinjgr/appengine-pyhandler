Thought appengine should have some basic IP based rate limiting. This has helped me deal with one user attempting to DoS a simple appengine site. You will still use some quota in this case, but it will be much less on a dynamic site.


Credit to http://www.thirumal.in/2012/04/sessions-in-google-app-engine-python.html for a great tutorial about custom session handlers.


Credit to https://github.com/jwarner112 for helping me figure out this idea.
