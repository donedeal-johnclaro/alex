import logging
import os

import requests
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template
from flask_ask import Ask, question, statement
load_dotenv(find_dotenv())


app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger('flask_ask').setLevel(logging.DEBUG)

ZIGBEE_URL = os.environ['ZIGBEE_URL']


@ask.launch
def god():
    job_question_msg = render_template('god')
    return question(job_question_msg)


@ask.intent('LightUpIntent')
def light_up():
    requests.post('{}/light/1'.format(ZIGBEE_URL))
    requests.post('{}/light/2'.format(ZIGBEE_URL))
    return statement('')


@ask.intent('LightDownIntent')
def light_down():
    requests.delete('{}/light/1'.format(ZIGBEE_URL))
    requests.delete('{}/light/2'.format(ZIGBEE_URL))
    return statement('')


if __name__ == '__main__':
    app.run(debug=True)
