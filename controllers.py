import tornado.web 

class index( tornado.web.RequestHandler ):
    def get( self ):
        self.render( "index.html" )

class member_apply( tornado.web.RequestHandler ):
    def get( self ): 
        self.render( "member/apply.html" )

class member_login( tornado.web.RequestHandler ):
    def get( self ):
        self.render( "member/login.html" )

class member_search( tornado.web.RequestHandler ):
    def get( self ):
        self.render( "member/search.html" )

class member_info( tornado.web.RequestHandler ):
    def get( self ):
        self.render( "member/info.html" )

class member_profile( tornado.web.RequestHandler ):
    def get( self, id ):
        self.render( "member/profile.html" )


