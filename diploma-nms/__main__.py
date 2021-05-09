import wsgiref.simple_server
import falcon

import random
import string

class MainController:
    def on_get(self, req, resp):
        resp.text = "".join(random.choice(string.digits) for i in range(1024))
        resp.status = falcon.HTTP_200


if __name__ == '__main__':
    app = application = falcon.App()
    app.add_route("/", MainController())

    with wsgiref.simple_server.make_server("", 4723, app) as httpd:
        print('Serving on port 4723...')
        httpd.serve_forever()
