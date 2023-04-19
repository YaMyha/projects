from flask import Flask, redirect
from connection import get_movie_by_title, get_movie_between, get_by_rating, get_by_genre

app = Flask(__name__)


@app.route("/movie/<title>")
def page_get_movie_by_title(title):
    data = get_movie_by_title(title)
    return f"""Название: {data["title"]}<br>
    Страна: {data["country"]}<br>
    Релиз: {data["release_year"]}<br>
    Жанр: {data["genre"]}<br>
    Описание: {data["description"]}"""


@app.route("/movie/<year_1>/to/<year_2>")
def page_get_movie_between(year_1, year_2):
    data = get_movie_between(year_1, year_2)
    return data


@app.route("/movie/rating/<rating>")
def page_get_movie_by_rating(rating):
    data = get_by_rating(rating)
    return data


@app.route("/movie/genre/<genre>")
def page_get_movie_by_genre(genre):
    data = get_by_genre(genre.capitalize())
    return data


app.run(debug=True)
