from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms import DecimalField, RadioField, SelectField, TextAreaField, FileField, SubmitField
from wtforms.validators import InputRequired, Length
from werkzeug.security import generate_password_hash # Converts password into encrypted hashes for security

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

class MyForm(FlaskForm):
    name = StringField('Name',validators=[InputRequired('Username Required!'),Length(min=5,max=25,message = "Username must be in 5 to 25 characters")])
    password = PasswordField('Password',validators=[InputRequired()])
    remember_me = BooleanField('Remember Me')
    salary = DecimalField('Salary',validators=[InputRequired()])
    gender = RadioField('Gender',choices=[('Male','male'),('Female','female')])
    country = SelectField('Country',choices=[('India','IN'),('United States of America','USA'),('United Kingdoms','UK')])
    message = TextAreaField('Message',validators=[InputRequired()])
    photo = FileField('Photo')
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        remember_me = form.remember_me.data
        salary = form.salary.data
        gender = form.gender.data
        country = form.country.data
        message = form.message.data
        photo = form.photo.data.filename
        return f'''Name:{name} <br> 
        Password:{generate_password_hash(password)} <br> 
        Remember me:{remember_me} <br> 
        Salary:{salary} <br> 
        Gender:{gender} <br> 
        Country:{country} <br> 
        Message:{message} <br> 
        Photo:{photo}'''
        # return f'Hi! {name}, your form is submitted Successfully'
    return render_template('form.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
