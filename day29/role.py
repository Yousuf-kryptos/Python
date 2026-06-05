from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user,current_user, login_required
from flask_security import Security, SQLAlchemyUserDatastore, roles_accepted, UserMixin, RoleMixin
from flask_security.utils import hash_password, verify_password
import uuid

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Password%401@localhost/taskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secretkey'
app.config['SECURITY_PASSWORD_SALT'] = 'my-password-salt'
app.config['SECURITY_PASSWORD_HASH'] = 'argon2'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'signin'

db = SQLAlchemy(app)

# Association Table

role_users = db.Table('role_users',
                      db.Column('user_id',db.Integer(),db.ForeignKey('user.id')),
                      db.Column('role_id',db.Integer(),db.ForeignKey('role.id')))

# Database Models
class User(db.Model,UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    email = db.Column(db.String(255), unique = True, nullable = False)
    password = db.Column(db.String(255), nullable = False, server_default = '')
    active = db.Column(db.Boolean(), default = True)
    fs_uniquifier = db.Column(db.String(255), unique = True, nullable = False, default = lambda:str(uuid.uuid4()))
    # Relationship with roles
    roles = db.relationship('Role',secondary = role_users, backref = 'users')

class Role(db.Model,RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique = True, nullable = False)

user_datastore = SQLAlchemyUserDatastore(db, User,Role)
security = Security(app,user_datastore)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/signup', methods=['GET','POST'])
def signup():
    msg = ''
    if request.method == 'POST':
        user = User.query.filter_by(email = request.form['email']).first()

        if user:
            msg = "User already exists"
            return render_template('signup.html',msg = msg)
        user = User(email = request.form['email'],password = hash_password(request.form['password']))
        role = Role.query.filter_by(id = int(request.form['options'])).first()
        if role:
            user.roles.append(role)
        else:
            msg = "Invalid User Selection"
            return render_template('signup.html', msg = msg)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('index'))
    return render_template('signup.html',msg = msg)

@app.route('/signin',methods=['GET','POST'])
def signin():
    msg = ''
    if request.method == 'POST':
        user = User.query.filter_by(email = request.form['email']).first()

        if user:
            if verify_password(request.form['password'], user.password):
                login_user(user)
                return redirect(url_for('index'))
            else:
                msg = 'Wrong Password'
        else:
            msg = "User doesn't exists"
        return render_template('signin.html', msg = msg)
    return render_template('signin.html', msg = msg)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# Teachers Route
@app.route('/teachers')
@login_required
@roles_accepted('Admin')
def teachers():
    teachers_list = []
    role_teachers = db.session.query(role_users).filter_by(role_id=2).all()
    for teacher in role_teachers:
        user = User.query.filter_by(id = teacher.user_id).first()
        if user:
            teachers_list.append(user)
    return render_template('teachers.html',teachers = teachers_list)

# Staff Route
@app.route('/staff')
@login_required
@roles_accepted('Admin','Teacher')
def staff():
    staff_list = []
    role_staff = db.session.query(role_users).filter_by(role_id = 3).all()
    for s in role_staff:
        user = User.query.filter_by(id = s.user_id).first()
        if user:
            staff_list.append(user)
    return render_template('staff.html',staff=staff_list)

# Student Route
@app.route('/students')
@login_required
@roles_accepted('Admin','Teacher','Staff')
def students():
    student_list = []
    role_students = db.session.query(role_users).filter_by(role_id = 4).all()
    for s in role_students:
        user = User.query.filter_by(id = s.user_id).first()
        if user:
            student_list.append(user)
    return render_template('student.html', students = student_list)

# My details Route
@app.route('/mydetails')
@login_required
@roles_accepted('Admin','Teacher','Staff','Student')
def mydetails():
    return render_template('mydetails.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)