from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

# Success Page
@app.route('/success')
def success():
    return "logged-in successfully"

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST' and request.form["username"] == "admin":
        return redirect(url_for("success"))
    
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)