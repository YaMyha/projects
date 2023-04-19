import logging

from flask import Blueprint, render_template, request
from coursework2.app.posts.dao.posts_dao import PostDao
from coursework2.config import PATH_POSTS, PATH_COMMENTS

logging.basicConfig(filename="api.log", level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
api_blueprint = Blueprint("api_blueprint", __name__, url_prefix="/api")

post_dao = PostDao(PATH_POSTS)

@api_blueprint.route("/posts")
def page_all_posts():
    logging.info("Запрос /api/posts")
    posts = post_dao.get_posts_all()
    return posts

@api_blueprint.route("/post/<int:pk>")
def page_post_by_post_id(pk):
    logging.info(f"Запрос /api/post/{pk}")
    post = post_dao.get_post_by_pk(pk)
    return post

