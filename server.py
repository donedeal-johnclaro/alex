import logging

from flask import Flask, render_template
from flask_ask import Ask, question


app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger('flask_ask').setLevel(logging.DEBUG)


@ask.launch
def welcome():
    welcome_msg = render_template('welcome')
    return question(welcome_msg)


if __name__ == '__main__':
    app.run(debug=True)
