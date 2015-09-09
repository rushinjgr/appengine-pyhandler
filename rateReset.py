__author__ = 'Justin Rushin III'

from google.appengine.api import memcache
from model.IpData import IpData
import datetime
import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        key_list = memcache.get(key="KEYLIST")
        the_now = datetime.datetime.now()
        if key_list is not None:
            for key in key_list:
                status = memcache.get(namespace="iprate", key=key)
                if status is not None:
                    newdata = IpData(modified=the_now, status=status, ip=key)
                    newdata.put()
            memcache.delete_multi(namespace="iprate", keys=key_list)
        k_l = ["0.0.0.0"]
        memcache.set(key="KEYLIST", value=k_l, time=4000)
    def post(self):
        self.get()

app = webapp2.WSGIApplication([
    ('/tasks/newrateReset', MainHandler)
], debug=True)
