from flask import Flask, request

app = Flask(__name__)

@app.before_request
def log_request():
    print(f"Incoming request: {request.method} {request.url}")

@app.after_request
def log_response(response):
    print(f"Outgoing Response: {response.status_code}")
    return response

@app.route('/')
def home():
    return "Welcome Home!"

if __name__ == '__main__':
    app.run(debug=True)