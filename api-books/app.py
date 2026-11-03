import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_migrate import Migrate

from db import db
from models.book import Book

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:postgres@localhost:5432/books",
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

# Campos que o PATCH pode alterar (protege o "id")
UPDATABLE_FIELDS = {
    "title", "author", "description",
    "is_favorite", "is_reading", "is_finished",
}


@app.route("/hello", methods=["GET"])
def hello():
    return "API está funcionando!"


@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()

    missing = [f for f in ("title", "author", "description") if f not in data]
    if missing:
        return jsonify({"error": f"Campos obrigatórios: {', '.join(missing)}"}), 400

    book = Book(
        title=data["title"],
        author=data["author"],
        description=data["description"],
    )
    db.session.add(book)
    db.session.commit()

    return jsonify({"message": "Livro inserido com sucesso"}), 201


@app.route("/books", methods=["GET"])
def get_all_books():
    books = Book.query.all()
    return jsonify([book.as_dict() for book in books])


@app.route("/books/<uuid:book_id>", methods=["GET"])
def get_book(book_id):
    book = db.get_or_404(Book, book_id)
    return jsonify(book.as_dict())


@app.route("/books/<uuid:book_id>", methods=["PATCH"])
def update_book(book_id):
    book = db.get_or_404(Book, book_id)
    data = request.get_json()

    for key, value in data.items():
        if key in UPDATABLE_FIELDS:
            setattr(book, key, value)

    db.session.commit()
    return jsonify({"message": "Livro atualizado com sucesso"})


@app.route("/books/<uuid:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = db.get_or_404(Book, book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Livro removido com sucesso"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
