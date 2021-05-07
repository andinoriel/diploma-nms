import wsgiref.simple_server

import falcon
import requests


class MainController:
    def on_get(self, req, resp):
        resp.text = "Greetings, traveller"
        resp.status = falcon.HTTP_200


if __name__ == '__main__':
    app = application = falcon.App()
    app.add_route("/", MainController())

    with wsgiref.simple_server.make_server('', 8000, app) as httpd:
        print('Serving on port 8000...')
        httpd.serve_forever()
