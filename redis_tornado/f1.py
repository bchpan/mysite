import tornado.web
import tornado.ioloop
import os
import redis

db = redis.StrictRedis() 

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        name = db.get('name')
        self.render('01/index.html', name=name)

    def post(self):
        name = self.get_argument('uname')
        db.set('name', name)
        self.redirect('/')


settings = dict(
        template_path = os.path.join(os.path.dirname("__file__"),
        'templates'),
    )

app = tornado.web.Application([
        (r'/',MainHandler),
    ], **settings)

if __name__ == "__main__":
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

