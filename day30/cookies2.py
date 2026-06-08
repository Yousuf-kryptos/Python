from flask import Flask, request, render_template, make_response

app = Flask(__name__)

@app.route('/',methods=['GET'])
def Login():
    return render_template('login1.html')

@app.route('/login1', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form)
        name = request.form['username']

        output = f"Hi {name}"

        res = make_response(output)
        res.set_cookie('username', name)

        return res

    return render_template('login1.html')

app.run(debug = True)
