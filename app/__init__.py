import controllers
import os.path

import tornado.web
import tornado.httpserver
import tornado.ioloop

import sys

settings = dict(      
   cookie_secret  =  "1234qwa4sxe5dtc6fryvtgbuhinj2w34ed5rft$)KJ(y",
   static_path    = os.path.join(os.path.dirname(__file__), "static"),
   template_path  = os.path.join(os.path.dirname(__file__), "views"),
)

application = tornado.web.Application( [
    ( "/",                          controllers.index           ),
    ( "/member/apply",              controllers.member_apply    ),
    ( "/member/login",              controllers.member_login    ),
    ( "/member/search",             controllers.member_search   ),
    ( "/member/info",               controllers.member_info     ),
    ( "/member/profile/(?P<id>.+)", controllers.member_profile  ),
], **settings )



#requires one command line argument, specifying the port to run on 
if __name__ == "__main__":
   assert len(sys.argv)==2 

   http_server = tornado.httpserver.HTTPServer(application, xheaders=True )

   listen_port = int(sys.argv[1])
   http_server.listen( listen_port )

   tornado.ioloop.IOLoop.instance().start()
