import logging
import os
import random

import requests
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template
from flask_ask import Ask, question, statement, session
load_dotenv(find_dotenv())


app = Flask(__name__)
ask = Ask(app, '/')
PEOPLE = {
    "Adam Curnow": "dog",
    "Adrian Acosta": "cat",
    "Aiden O'Byrne": "dog",
    "Alex Geronimo": "dog",
    "Amanda Thornton": "dog",
    "Andras Kurucz": "cat",
    "Anneliese Schnittger": "cat",
    "Aoife McCormack": "cat",
    "Aoife O' Brien": "cat",
    "Arunkumar Aousula": "dog",
    "Barry Connaughton": "cat",
    "Barry Murphy": "dog",
    "Bartosz Zolynski": "dog",
    "Ben Cowley": "dog",
    "Bill Kastanakis": "dog",
    "Bill Tector": "cat",
    "Boyana Boneva": "dog",
    "Brian Fallon": "cat",
    "Brian Kinsella": "cat",
    "Cameron": "dog",
    "Claire Doyle": "cat",
    "Colm Carew": "dog",
    "Conor O'Brien": "cat",
    "Conor Smith": "cat",
    "Cristian Moisa": "dog",
    "Dan Whelan": "dog",
    "Daniel Good": "dog",
    "Danny Kehoe": "dog",
    "Dara O'Leary": "cat",
    "David Ashford": "cat",
    "David Conde": "dog",
    "David Phelan": "cat",
    "Declan Lawlor": "cat",
    "Derek Cheung": "cat",
    "Diarmaid Fallon": "cat",
    "Diarmuid MacNamara": "dog",
    "Eamonn Fallon": "dog",
    "Emma Hunt": "dog",
    "Ernesto Fernandez": "cat",
    "Esteban Walsh": "cat",
    "Eve Makarova": "cat",
    "External Test": "dog",
    "Fabio Mignogna": "cat",
    "Finbarr Garland": "cat",
    "Gabor Zelei": "cat",
    "Gabriel de Tassigny": "cat",
    "Gareth Davies": "cat",
    "Gary Doolin": "cat",
    "Gary Meehan": "cat",
    "Gustavo Godoi": "dog",
    "Hilda O'Brien": "dog",
    "Jana Platau-Wagner": "dog",
    "Jason Blood": "cat",
    "Jenny Franklin": "dog",
    "Jenny O'Sullivan": "dog",
    "Jessa Pajarito": "cat",
    "Joao Moreira": "cat",
    "John Brennan": "cat",
    "John Claro": "dog",
    "John Needham": "dog",
    "Judyta Holubowicz": "dog",
    "Julia Maurer": "dog",
    "Kerrie Ryan": "dog",
    "Laura Doyle": "cat",
    "Laura Lacey": "cat",
    "Lisa McDonnell": "cat",
    "Luan Reffatti": "dog",
    "Luke Cassidy": "dog",
    "Maeve Carey": "cat",
    "Maghnus O'Kane": "dog",
    "Mahmoud Mohamed": "cat",
    "Mario Magdic": "cat",
    "Martin Peters": "dog",
    "Maurizio Crespi": "dog",
    "Melanie Doyle": "dog",
    "Milen Dobrev": "dog",
    "Nerijus Urbietis": "cat",
    "Noel Tate": "dog",
    "Padraig Howlin": "dog",
    "Paul Harrington": "cat",
    "Paula Tierney": "dog",
    "Peter Burrows": "cat",
    "Priyanka Sonkar": "cat",
    "Renata Marini": "cat",
    "Rob Hume": "cat",
    "Roisin": "cat",
    "Ronan Doyle": "dog",
    "Ronan O Keeffe": "dog",
    "Ronan O'Neill": "dog",
    "Sarah Downey": "dog",
    "Sean Culleton": "dog",
    "Sean Reddin": "cat",
    "Sergio Bestetti": "dog",
    "Shane Fox": "cat",
    "Simon Andreucetti": "cat",
    "Stephen O'Neill": "dog",
    "Stephen O'Reilly": "cat",
    "apollo-bot": "dog",
    "superscouse": "dog"
}

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


@ask.intent('JobQuestionIntent')
def job_question():
    random_person = random.choice(PEOPLE.keys())
    job_question_msg = render_template('job_question', person=random_person)
    session.attributes['person'] = random_person

    return question(job_question_msg)


@ask.intent('JobAnswerIntent', convert={'job': str})
def job_answer(job):
    correct_person = session.attributes['person']
    correct_job = PEOPLE[correct_person]
    
    print '----------------------------------------------------------------------------------------'
    print job
    print '----------------------------------------------------------------------------------------'
    if correct_job.lower() == job:
        job_answer_msg = render_template('correct_job_answer')
    else:
        job_answer_msg = render_template('wrong_job_answer', person=correct_person, job=correct_job)
    
    return statement(job_answer_msg)


if __name__ == '__main__':
    app.run(debug=True)
