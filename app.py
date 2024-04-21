from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {'id' : 1, 'title' : 'Book1', 'author' : 'Author1'},
    {'id' : 2, 'title' : 'Book2', 'author' : 'Author2'},
    {'id' : 3, 'title' : 'Book3', 'author' : 'Author3'},
]

@app.route('/book', methods = ['GET'])
def book_all():
    return jsonify(books)

@app.route('/book/<int:book_id>', methods = ['GET'])
def book_one(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
    return jsonify({'Error' : f'There are no book with ID {book_id}'})

@app.route('/send_book', methods =['POST'])
def insert_book():
    book_id = len(books) + 1
    new_book = {'id' : book_id, 'title' : request.json['title'], 'author' : request.json['author']}
    books.append(new_book)
    return jsonify({'Succesful' : f'New book with ID {book_id} succesful added'})


@app.route('/update_book/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book['id']==book_id:
            book['title']=request.json['title']
            book['author']=request.json['author']
            return jsonify({'Succesful' : f'Book with ID {book_id} succesful update'}) 
    return jsonify({'Error' : f'There are no book with ID {book_id}'})

@app.route('/delete_book/<int:book_id>', methods = ['DELETE'])
def delet_book(book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
    return jsonify({'Succesful' : f'Book with ID {book_id} succesful delete'})

if __name__ == "__main__":
    app.run(debug=True)