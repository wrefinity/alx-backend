#!/usr/bin/env python3
"""Flask app"""
from flask import (
    Flask,
    render_template,
    request
)
from flask_babel import Babel


class Config(object):
    """
    Babel Config
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale()-> str:
    """ retrives the local for a page"""
    queries = request.query_string.decode('utf-8').split('&')
    query_lst = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        queries,
    ))
    if 'locale' in query_lst:
        if query_lst['locale'] in app.config["LANGUAGES"]:
            return query_lst['locale']
    return request.accept_languages.best_match(app.config["LANGUAGES"])



@app.route('/', strict_slashes=False)
def index() -> str:
    """entry point"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
