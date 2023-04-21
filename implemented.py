from dao.book import BookDAO
from dao.author import AuthorDAO
from dao.genre import GenreDAO
from service.book import BookService
from service.author import AuthorService
from service.genre import GenreService
from setup_db import db

book_dao = BookDAO(session=db.session)
author_dao = AuthorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)

book_service = BookService(dao=book_dao)
author_service = AuthorService(dao=book_dao)
genre_service = GenreService(dao=book_dao)