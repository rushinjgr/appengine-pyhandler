from google.appengine.ext import ndb


class IpData(ndb.Model):
    modified = ndb.DateTimeProperty()
    ip = ndb.StringProperty()
    status = ndb.IntegerProperty()


