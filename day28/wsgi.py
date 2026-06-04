# class WSGILoggingMiddleware:
#     def __init__(self,app):
#         self.app = app
    
#     def __call__(self, environ, start_response):
#         print(f"Incoming request: {environ['REQUEST_METHOD']} {environ['PATH_INFO']}")
#         return self.app(environ,start_response)
    
# from flask import Flask

# app = Flask(__name__)
# app.wsgi_app = WSGILoggingMiddleware(app.wsgi_app)

# @app.route('/')
# def home():
#     return "Hello, WSGI Middleware"

# if __name__ == '__main__':
#     app.run(debug=True)

from werkzeug.middleware.proxy_fix import ProxyFix
from flask import Flask

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app,x_for=1,x_proto=1,x_host=1,x_port=1,x_prefix=1)

@app.route('/')
def home():
    return "ProxyFix Middleware Applied!"

if __name__ == '__main__':
    app.run(debug=True)