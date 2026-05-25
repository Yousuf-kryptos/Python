# # Flask 
# from flask import Flask,request,render_template

# app = Flask(__name__) # Creates Flask Application

# @app.route('/login',methods=['GET','POST']) # Connects home url('/') to the function
# def login():
#     if request.method == 'POST':
#         name = request.form['username']
#         return f"Hello {name},POST request received"
#     return render_template('name.html')

# if __name__ == '__main__':
#     app.run(debug=True)  # starts local server

from flask import Flask

app = Flask(__name__)

@app.route('/number/<int:id>') # Specify the datatype
def num(id):
    return f"Id of the post is {id}"

@app.route('/user/<username>')
def show_user(username):
    return f"Hi, {username}"

@app.route('/')
def homepage():
    return "Homepage"

@app.route('/greet')
def greet():
    return "Welcome Yousuf"

# # add_url_rule function demo
# def view_users(username):
#     return f"Hi, {username}"

# app.add_url_rule('/user/<username>','view_users',view_users)

if __name__ == '__main__':
    app.run(debug = True)