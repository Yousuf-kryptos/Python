from flask import Flask, request
from flask_restful import Resource, Api

# app = Flask(__name__)
# api = Api(app)

# class demo(Resource):
#     def get(self):
#         return{"message":"Hello, Good Morning"}
    
# api.add_resource(demo,'/')

# if __name__ == '__main__':
#     app.run(debug=True)

app = Flask(__name__)
api = Api(app)

books = [
    {"id": 1, "title": "Concept of Physics", "author": "H.C Verma"},
    {"id": 2, "title": "Gunahon ka Devta", "author": "Dharamvir Bharti"},
    {"id": 3, "title": "Problems in General Physics", "author": "I.E Irodov"}
]

class BookResource(Resource):
    def get(self,book_id = None):
        if book_id is None:
            return books, 200 # Explicitly return status 200 ok
        
        book = next((book for book in books if book['id'] == book_id ), None)
        if book:
            return book,200
        return {'error':'Book not found'}, 404 # Return 404 only when not found
    
    def post(self):
        new_book = request.json
        books.append(new_book)
        return new_book,201  # Created Successfully
    
    def put(self,book_id):
        book = next((book for book in books if book['id'] == book_id),None)
        if not book:
            return {'error':'Book not found'}, 404
        
        data = request.json
        book.update(data)
        return book, 200
    
    def delete(self, book_id):
        global books
        book = [book for book in books if book['id']!=book_id]
        return {'message':'Book deleted'}
    
api.add_resource(BookResource,'/','/<int:book_id>')

if __name__ == '__main__':
    app.run(debug=True)
