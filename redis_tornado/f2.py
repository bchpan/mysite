import os
import tornado.web
import tornado.ioloop
import tornado.httpserver
import redis

class App(tornado.web.Application):
    def __init__(self):
        handlers = [
                (r'/', MainHandler), 
            ]

        settings = dict(
                template_path = os.path.join(os.path.dirname("__file__"), 'templates')
            )

        tornado.web.Application.__init__(self, handlers, **settings)

        self.db = redis.StrictRedis()


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db


class MainHandler(BaseHandler):
    def get(self):
        name = self.db.get('name')
        self.render('01/index.html', name=name)

    def post(self):
        name = self.get_argument('uname')
        self.db.set('name', name)
        self.redirect('/')

def main():
    http_server = tornado.httpserver.HTTPServer(App())
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
        main()

