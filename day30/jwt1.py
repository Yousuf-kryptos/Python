from flask import Flask, redirect, url_for, request, render_template, jsonify, make_response
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
import jwt
import uuid
from datetime import datetime, timezone, timedelta
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Password%401@localhost/taskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users1'
    id = db.Column(db.Integer, primary_key = True)
    public_id = db.Column(db.String(50), unique = True, nullable = False)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    password = db.Column(db.String(255), nullable = False)

def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = request.cookies.get('jwt_token')

        if not token:
            return jsonify({'message':'Token is missing'}), 401
        
        try:
            data = jwt.decode(
                token,
                app.config['SECRET_KEY'],
                algorithms=['HS256']
            )

            current_user = User.query.filter_by(public_id = data['public_id']).first()

            if not current_user:
                return jsonify({'message':'User not found'}), 401
            
        except jwt.ExpiredSignatureError:
            return jsonify({'message':'Token has expired'}), 401
        
        except jwt.InvalidTokenError:
            return jsonify({'message':'Invalid Token'}), 401
        
        return f(current_user, *args, **kwargs)
    return decorated

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email = email).first()

        if not user:
            return jsonify({
                'message':'Invalid email or password'
            }), 401
        
        if not check_password_hash(user.password,password):
            return jsonify({
                'message':'Invalid email or password'
            }), 401
        
        token = jwt.encode({
            'public_id': user.public_id,
            'exp':datetime.now(timezone.utc) + timedelta(hours=1)
        },
        app.config['SECRET_KEY'],
        algorithm='HS256'
        )

        response = make_response(
            redirect(url_for('dashboard'))
        )

        response.set_cookie(
            'jwt_token',
            token,
            httponly=True,
            samesite='Lax'        
            )
        
        return response
    return render_template('login.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        existing_user = User.query.filter_by(email = email).first()

        if existing_user:
            return jsonify({
                'message':'User alreadt exists. Please login'
            }), 400
        
        hashed_password = generate_password_hash(password)

        new_user = User(
            public_id = str(uuid.uuid4()),
            name = name,
            email = email,
            password = hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/dashboard')
@token_required
def dashboard(current_user):
    return f"""
            <h1>Welcome {current_user.name}!</h1>
            <p>You are logged in Successfully</p><br>
            <a href="/users">All Users</a><br>
            <a href="/logout">logout</a>"""

@app.route('/logout')
def logout():
    response = make_response(
        redirect(url_for('login'))
    )

    response.delete_cookie('jwt_token')

    return response

@app.route('/users')
def users():
    all_users = User.query.all()

    user_list = []

    for user in all_users:
        user_list.append({
            'id':user.id,
            'name':user.name,
            'email':user.email
        })
    
    return jsonify(user_list)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)