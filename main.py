from flask import Flask
from flask_restx import Api

from config import Config
from views.books import book_ns
from views.authors import author_ns
from views.genres import genre_ns
from setup_db import db

from dao.model.book import Book
from dao.model.author import Author
from dao.model.genre import Genre


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.app_context().push()
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(book_ns)
    api.add_namespace(author_ns)
    api.add_namespace(genre_ns)
    # create_data(app, db)


def create_db():
    book_1 = Book(id=1, name='Book_1', description="Desc_1", year=2023, rating="NC-17", genre_id=1, author_id=1)
    book_2 = Book(id=2, name='Book_2', description="Desc_2", year=2023, rating="NC-17", genre_id=2, author_id=2)
    add_list_b = [book_1, book_2]

    genre_1 = Genre(id=1, name='detective')
    genre_2 = Genre(id=2, name='novel')
    add_list_g = [genre_1, genre_2]

    author_1 = Author(id=1, name='Author_1')
    author_2 = Author(id=2, name='Author_2')
    add_list_a = [author_1, author_2]

    db.create_all()
    with db.session.begin():
        db.session.add_all(add_list_a)
        db.session.add_all(add_list_b)
        db.session.add_all(add_list_g)

    print(db.session.query(Book).all())
    print(db.session.query(Author).all())
    print(db.session.query(Genre).all())


app = create_app(Config())
create_db()
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
