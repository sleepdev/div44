import tornado.web 

class index( tornado.web.RequestHandler ):
    def get( self ):
        self.render( "index.html" )

class profile( tornado.web.RequestHandler ):
    def get( self, id ):
        self.render( "profile.html" )

class search( tornado.web.RequestHandler ):
    def get( self ):
        self.render( "search.html" )

