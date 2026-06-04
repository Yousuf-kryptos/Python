from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app,origins=["http://localhost:3000","https://myfrontend.com/"])

@app.route('/public-data')
def public_data():
    return jsonify({"message":"This data is accessible from allowed origins"})

@app.route('/private-data')
def private_data():
    return jsonify({"message":"This endpoint also follows CORS rules"})

if __name__ == '__main__':
    app.run(debug=True)