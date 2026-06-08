# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/submit',methods = ['POST'])
# def receive_data():
#     data = request.get_json()
#     return {"message":"Data Received", "Data":data}

# if __name__ == '__main__':
#     app.run(debug=True)

# Using Marshmallow

from flask import Flask, request, jsonify
from marshmallow import Schema, fields

app = Flask(__name__)

class UserSchema(Schema):
    username = fields.String(required=True)
    email = fields.String(required=True)

user_schema = UserSchema()

@app.route('/validate',methods=['POST'])
def validate_user():
    json_data = request.get_json()
    errors = user_schema.validate(json_data)

    if errors:
        return jsonify(errors), 400
    
    return jsonify({'message':'valid data', 'data':json_data})

if __name__ == '__main__':
    app.run(debug=True)
