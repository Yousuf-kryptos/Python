from flask import Flask

app = Flask(__name__)

@app.route('/')
def msg():
    return "Welcome Home!"

# String Variable - default
@app.route('/vstring/<name>')
def show_name(name):
    return f"Hi, {name}"

# Integer Variable
@app.route('/vint/<int:id>')
def show_id(id):
    return f"My ID is {id}"

# Float Variablr
@app.route('/vfloat/<float:price>')
def show_price(price):
    return f"I have Rs.{price}"

if __name__ == '__main__':
    app.run(debug=True)