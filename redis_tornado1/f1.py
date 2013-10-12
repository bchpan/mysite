import os
import redis
import tornado.web
import tornado.ioloop
import tornado.httpserver

class App(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/add', BlogAddHandler),
            (r'/view/(\d+)', BlogViewHandler)
        ]

        settings = dict(
            template_path = os.path.join(os.path.dirname('__file__'), 'templates'),
        )

        tornado.web.Application.__init__(self, handlers, **settings)

        self.db = redis.StrictRedis()


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db



class BlogAddHandler(BaseHandler):
    def get(self):
        self.render('06/add.html')
        #self.write('06/add.html')

    def post(self):
        title = self.get_argument('title')    
        content = self.get_argument('content')    
        author = self.get_argument('author')    
        slug = self.get_argument('slug')

        blog_id = self.db.incr('blogs:count')
        isSlugAvailable = self.db.hsetnx('slug.to.id', slug, blog_id)

        if isSlugAvailable == 0:
            self.db.decr('blog:count')
            exit

        self.db.hmset('blog:%s'%blog_id, 
            {'title':title, 'content':content, 'author':author, 'slug':slug}
        )

        self.redirect('/view/%s' % blog_id)

class BlogViewHandler(BaseHandler):
    def get(self, blog_id):
        blog = self.db.hgetall('blog:%s'%blog_id)
        
        if not blog:
            raise tornado.web.HTTPError(404)
        
        views = self.db.hincrby('blog:%s'%blog_id, 'views')
        
        self.render('06/view.html', title=blog['title'], content=blog['content'], author=blog['author'], slug=blog['slug'])
        

def main():
    http_server = tornado.httpserver.HTTPServer(App())
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()

