from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # use %40 instead of @ in password Ex:Password@1 -> Password%401
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # To avoid Warnings

db = SQLAlchemy(app)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20), unique = False, nullable = False)
    last_name = db.Column(db.String(20), unique = False, nullable = False)
    age = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"Name: {self.first_name}, Age: {self.age}"
    
@app.route('/')
def index1():
    profiles = Profile.query.all()
    return render_template('index1.html',profiles = profiles)

@app.route('/add_data')
def add_data():
    return render_template('add_profile.html')

@app.route('/add',methods=["POST"])
def profile():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    age = request.form.get("age")

    if first_name != '' and last_name != '' and age is not None:
        p = Profile(first_name=first_name, last_name=last_name, age=age)
        db.session.add(p)
        db.session.commit()
        return redirect('/')
    else:
        return redirect('/')
    
@app.route('/delete/<int:id>')
def erase(id):
    data = db.session.get(Profile,id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():  # Need for database operations
        db.create_all()      # creates the database and tables
    app.run(debug=True)