from flask import Flask, render_template, request
from babel import numbers, dates
from datetime import datetime, time, date
from flask_babel import Babel, gettext
app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)


@babel.localeselector
def get_locale():
    #result = request.accept_languages.best_match(['en', 'es', 'de'])
    return 'es'


@app.route('/')
def index():
    return gettext("Please translate me ,") + ' ' + gettext('My name is %(name)s.', name='Charan')

if __name__ == '__main__':
    app.run()
