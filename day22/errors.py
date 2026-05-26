from flask import Flask, abort

app = Flask(__name__)

@app.route('/<uname>')
def index(uname):
    if uname[0].isdigit():
        # abort(400)
        abort(403)
    return '<h1>Good usernames</h1>'

if __name__ == '__main__':
    app.run(debug=True)