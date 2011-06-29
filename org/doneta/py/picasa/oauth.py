#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 2011-6-27
# @author: Key Dai

import tornado.ioloop
import tornado.web
from oauth2client.client import OAuth2WebServerFlow

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        flow = OAuth2WebServerFlow(
                  # Visit https://code.google.com/apis/console to
                  # generate your client_id, client_secret and to
                  # register your redirect_uri.
                  client_id='720258124919-1o4glqsk2s8gghht9kepstoqac0rcg5b.apps.googleusercontent.com',
                  client_secret='EoQKmmIffrOzQ1QNsg4eis7D',
                  scope='https://picasaweb.google.com/data/',
                  user_agent='buzz-cmdline-sample/1.0')
        authorize_url = flow.step1_get_authorize_url("http://localhost:8888/callback")
        self.redirect(authorize_url)
        

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()