import logging
from random import randint

from flask import Flask, render_template
from flask_ask import Ask, question, statement, session


app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger('flask_ask').setLevel(logging.DEBUG)


@ask.launch
def welcome():
    welcome_msg = render_template('welcome')
    return question(welcome_msg)


@ask.intent('JobIntent', convert={'person': str})
def next_round(person):
    job = 'Professional athlete'
    round_msg = render_template('job', person=person, job=job)
    return statement(round_msg)


if __name__ == '__main__':
    app.run(debug=True)
