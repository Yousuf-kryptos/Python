from flask import Flask, jsonify, request

app =Flask(__name__)

@app.route('/returnjson',methods=['GET'])
def return_json():
    data = {
        "module":15,
        "subject":"DSA"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)