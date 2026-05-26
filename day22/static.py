from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    message = "Good Morning"
    return render_template('home1.html',message=message)

@app.route('/image')
def serve_images():
    message = "Image Route"
    return render_template('image.html',message=message)

if __name__ == '__main__':
    app.run(debug=True)