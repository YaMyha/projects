import sqlite3
from collections import Counter
import json

def get_movie_by_title(movie_title):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""select title, country, release_year, listed_in, description
                   from netflix
                   where title = '{movie_title}'
                   order by release_year desc
                   limit 1"""
        cursor.execute(query)
        data = cursor.fetchone()
        result = {
            "title": data[0],
            "country": data[1],
            "release_year": data[2],
            "genre": data[3],
            "description": data[4]
        }
        return result


def get_movie_between(first_year, second_year):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""select title, release_year
                   from netflix
                   where release_year between {first_year} and {second_year}
                   limit 100"""
        cursor.execute(query)
        data = cursor.fetchall()
        result = []
        for item in data:
            result.append({"title": item[0], "release_year": item[1]})
        return result


def get_by_rating(rating):
    rating_list = {"children": "'G'",
                   "family": "'G', 'PG', 'PG-13'",
                   "adult": "'R', 'NC-17'"}
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""select title, rating, release_year
                   from netflix
                   where rating in ({rating_list[rating]})
                   limit 100"""
        cursor.execute(query)
        data = cursor.fetchall()
        result = []
        for item in data:
            result.append({"title": item[0], "rating": item[1], "release_year": item[2]})
        return result


def get_by_genre(genre):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""select title, description
                   from netflix
                   where listed_in like '%{genre}%'
                   limit 10"""
        cursor.execute(query)
        data = cursor.fetchall()
        result = []
        for item in data:
            result.append({"title": item[0], "description": item[1]})
        return result


def get_actors_by_actor_pair(actor_1, actor_2):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""select "cast"
                   from netflix
                   where "cast" like ? and "cast" like ?"""
        cursor.execute(query, (f'%{actor_1}%', f'%{actor_2}%',))
        data = cursor.fetchall()
        actors_played = []
        for cast in data:
            actors_played.extend(cast[0].split(', '))
        counter = Counter(actors_played)
        result = []
        for actor, count in counter.items():
            if actor not in [actor_1, actor_2] and count > 2:
                result.append(actor)
        return result


def get_by_type_genre_release_year(movie_type, genre, release_year):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""select title, description, type, listed_in, release_year
                   from netflix
                   where type like ? and listed_in like ? and release_year = ?"""
        cursor.execute(query, (f'%{movie_type}%', f'%{genre}%', f'{release_year}',))
        data = cursor.fetchall()
        movies = []
        for movie in data:
            movies.append({"title": movie[0], "description": movie[1]})
        return json.dumps(movies)


g = get_by_type_genre_release_year('TV Show', 'Dramas', '2020')

1