from google.appengine.api import memcache
import webapp2


class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        hour_limit = 400
        ip = self.request.remote_addr
        print(ip)
        key_list = memcache.get(key="KEYLIST")
        if key_list is not None and ip not in key_list:
            key_list.append(ip)
            memcache.set(key="KEYLIST", value=key_list)
        elif key_list is None:
            k_l = [ip]
            memcache.set(key="KEYLIST", value=k_l, time=4000)
        res = memcache.get(key=ip,namespace="iprate")
        if res is None:
            # add ip to memcache
            memcache.set(key=ip, value=1, namespace="iprate", time=3900)
            # fulfill request
            webapp2.RequestHandler.dispatch(self)
        else:
            if res < 0:
                # user is flagged
                # error out
                self.response.write(429)
            else:
                # user is not flaggged
                if res < hour_limit:
                    # user is at/below rate limit
                    # increment requests
                    res += 1
                    # store to memcache
                    memcache.set(key=ip,value=res,namespace="iprate",time=3900)
                    # dispatch req
                    webapp2.RequestHandler.dispatch(self)
                else:
                    # user is in excess of rate limit
                    # flag user
                    res = -1
                    # error out
                    memcache.set(key=ip, value=res, namespace="iprate", time=3900)
                    self.response.write(429)


