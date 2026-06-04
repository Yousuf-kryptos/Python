from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
from werkzeug.security import generate_password_hash,check_password_hash
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Password@1'
app.config['MYSQL_DB'] = 'taskdb'

mysql = MySQL(app)

@app.route('/login',methods=['GET','POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']


        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM students WHERE username = %s',(username,))

        student = cursor.fetchone()

        if student and check_password_hash(student['password'],password):
            session['loggedin'] = True
            session['username'] = student['username']
            session['email'] = student['email']
            msg = 'Logged in Successfully'
            return render_template('index.html',msg=msg)
        else:
            msg = "Incorrect username / password"
            return redirect(url_for('home'))
    return render_template('login.html',msg = msg)

@app.route('/register',methods=['GET','POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM students WHERE email = %s',(email,))
        student = cursor.fetchone()

        hashed_password = generate_password_hash(password)

        if student:
            msg = 'EmailID already exists'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+',email):
            msg = 'Invalid Email Address'
        elif not re.match(r'^[a-zA-Z0-9]+$',username):
            msg = 'Alphabets and numbers only allowed'
        elif not username or not password or not email:
            msg = 'Invalid username/password/email'
        else:
            cursor.execute('INSERT INTO students VALUES(NULL,%s,%s,%s)',(username,hashed_password,email))
            mysql.connection.commit()
            msg = 'You have successfully registered'
    elif request.method == 'POST':
        msg = 'Please fill the form'
    return render_template('register.html',msg = msg)

@app.route('/logout')
def logout():
    session.pop('loggedin',None)
    session.pop('username',None)
    session.pop('password',None)
    session.pop('email',None)
    return redirect(url_for('login'))

@app.route('/')
def home():
    if 'loggedin' in session:
        return render_template('index.html')
    return redirect(url_for('login'))
if __name__ == '__main__':
    app.run(debug=True)