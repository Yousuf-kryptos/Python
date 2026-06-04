from flask import Flask, request, jsonify

app = Flask(__name__)

API_KEY = "my_secret_api_key"

@app.before_request
def log_request():
    print(f"Incoming request: {request.method} {request.url}")

@app.before_request
def check_authentication():
    token = request.headers.get('Authorization')
    if token != f"Bearer {API_KEY}":
        return jsonify({"error":"Unauthorized"}), 401

@app.after_request
def log_response(response):
    print(f"Outgoing Response: {response.status_code}")
    return response

@app.route('/secure-data')
def secure_data():
    return jsonify({"message":"Access granted to secure data"})

if __name__ == '__main__':
    app.run(debug=True)