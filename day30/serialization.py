from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data')
def demo():
    data = {"name":"yousuf", "age":22, "city": "Chennai"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

# import json

# data = {"name":"yousuf", "age":22, "city": "Chennai"}
# json_data = json.dumps(data)
# print(json_data)