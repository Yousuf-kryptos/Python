from flask import Flask
from flask_restful import Api,Resource

app =Flask(__name__)

api = Api(app)

class ReturnJSON(Resource):
    def get(self):
        data = {
            "module":15,
            "subject":"DSA"
        }
        return data
    
api.add_resource(ReturnJSON,'/returnjson')

if __name__ == '__main__':
    app.run(debug=True)