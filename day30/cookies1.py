from flask import Flask, request, make_response

app = Flask(__name__)

# Setting the cookie
@app.route('/')
def setcookie():
    resp = make_response('Setting the cookie')
    resp.set_cookie('Yousuf','Aasik')
    return resp

# Getting the cookie
@app.route('/getcookie')
def getcookie():
    result = request.cookies.get('Yousuf')
    return 'My name is '+result

app.run()