from flask import Flask, request, render_template, url_for, redirect
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, UserMixin, login_required, current_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretkey'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Password@1'
app.config['MYSQL_DB'] = 'taskdb'

mysql = MySQL(app)

# Flask-login Setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self,id,username):
        self.id = id
        self.username = username

@login_manager.user_loader
def load_user(user_id):
    cursor = mysql.connection.cursor()

    cursor.execute('SELECT id, username FROM accounts WHERE id = %s',(user_id,))

    account = cursor.fetchone()
    cursor.close()

    if account:
        return User(account[0],account[1])
    
    return None

@app.route('/register',methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        cursor = mysql.connection.cursor()

        cursor.execute('SELECT * FROM accounts WHERE username = %s',(username,))

        existing_user = cursor.fetchone()

        if existing_user:
            cursor.close()
            return render_template('register.html',error="Username already taken")
        
        hashed_password = generate_password_hash(password)

        cursor.execute('INSERT INTO accounts VALUES (NULL,%s,%s,%s)',(username,hashed_password,email))

        mysql.connection.commit()

        cursor.close()

        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor()

        cursor.execute('SELECT * FROM accounts WHERE username = %s',(username,))

        account = cursor.fetchone()

        if account and check_password_hash(account[2],password):
            login_user(User(account[0],account[1]))
            return redirect(url_for('dashboard'))
        
        return render_template('login.html',error = "Invalid username or password")
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html',username=current_user.username)

@app.route('/logout')
@login_required
def logout():
    logout_user()

    return(redirect(url_for('login')))

if __name__ == '__main__':
    app.run(debug=True)