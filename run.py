from flask import Flask

from coursework2.app.views import post_blueprint
from coursework2.api import api_blueprint

app = Flask(__name__)

app.register_blueprint(post_blueprint)
app.register_blueprint(api_blueprint)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Страница не найдена</h1>", 404


@app.errorhandler(500)
def page_not_found(e):
    return 500


if __name__ == "__main__":
    app.run(debug=True)
