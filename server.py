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
    people = {
        "Adam Curnow": "IT Support Intern",
        "Adrian Acosta": "CEO Journal Media",
        "Aiden O'Byrne": "",
        "Alex Geronimo": "The Bringer of Craic",
        "Amanda Thornton": "Head of Customer Support",
        "Andras Kurucz": "Android Developer",
        "Anneliese Schnittger": "Customer Services Manager - Daft.ie",
        "Aoife McCormack": "Motor Customer Support Manager",
        "Aoife O' Brien": "QA Intern (DoneDeal.ie)",
        "Arunkumar Aousula": "QA Automation Engineer @ P&M Team",
        "Barry Connaughton": "Guest",
        "Barry Murphy": "Engineering Manager - Frontend",
        "Bartosz Zolynski": "Engineer Manager - Backend (Daft.ie)",
        "Ben Cowley": "Frontend Developer (DoneDeal.ie)",
        "Bill Kastanakis": "Engineering Manager | Mobile",
        "Bill Tector": "UX Design and Research",
        "Boyana Boneva": "QA Engineer",
        "Brian Fallon": "Motor & Property",
        "Brian Kinsella": "Junior Quality Engineer",
        "Cameron": "",
        "Claire Doyle": "",
        "Colm Carew": "Java Dev",
        "Conor O'Brien": "Android Developer",
        "Conor Smith": "Android dev (thejournal)",
        "Cristian Moisa": "QA Engineer Property Team",
        "Dan Whelan": "Senior Designer",
        "David Ashford": "Wizard",
        "Daniel Good": "Head of Marketplaces",
        "Danny Kehoe": "Junior Java Dev",
        "Dara O'Leary": "HR Business Partner Wexford/Waterford",
        "David Conde": "Architect",
        "David Phelan": "Key Account Manager",
        "Declan Lawlor": "CTA",
        "Derek Cheung": "Android Developer",
        "Diarmaid Fallon": "Financial Accountant",
        "Diarmuid MacNamara": "Site Reliability Engineer",
        "Eamonn Fallon": "CEO Distilled SCH",
        "Emma Hunt": "",
        "Ernesto Fernandez": "iOS Developer",
        "Esteban Walsh": "iOS Developer @ DoneDeal.ie",
        "Eve Makarova": "Product Manager @Adverts @DoneDeal",
        "External Test": "I test integrations",
        "Fabio Mignogna": "Senior iOS Developer 2",
        "Finbarr Garland": "Trust & Safety",
        "Gabor Zelei": "Innocent Bystander",
        "Gabriel de Tassigny": "Backend developer",
        "Gareth Davies": "Snr UX Designer",
        "Gary Doolin": "Android Developer",
        "Gary Meehan": "Frontend @ DoneDeal",
        "Gustavo Godoi": "Frontend developer at @Donedeal.ie",
        "Hilda O'Brien": "",
        "Jana Platau-Wagner": "Programme Manager",
        "Jason Blood": "Mobile Lead",
        "Jenny Franklin": "Lead Design",
        "Jenny O'Sullivan": "Adverts Customer Support",
        "Jessa Pajarito": "Junior Android Developer",
        "Joao Moreira": "Software Engineer @ Property (Daft.ie)",
        "John Brennan": "Frontend Developer @ P&M team",
        "John Claro": "Graduate Data Engineer",
        "John Needham": "Head of Engineering - Journal Media",
        "Judyta Holubowicz": "Chief Product Officer",
        "Julia Maurer": "Monetization Marketplaces @Distilled SCH",
        "Kerrie Ryan": "Digital Content Exec",
        "Laura Doyle": "Head of HR",
        "Laura Lacey": "Executive Assistant & Office Manager",
        "Lisa McDonnell": "Business Development Executive",
        "Luan Reffatti": "Java Developer",
        "Luke Cassidy": "Systems Engineering Manager @Marketplaces",
        "Maeve Carey": "Technical Project Manager",
        "Maghnus O'Kane": "Unabashed Goldfish",
        "Mahmoud Mohamed": "Systems admin",
        "Mario Magdic": "Software Engineer @ adverts.ie",
        "Martin Peters": "Head of Analytics & Data Services",
        "Maurizio Crespi": "Adverts Systems Engineer",
        "Melanie Doyle": "Junior Designer Motor Team",
        "Milen Dobrev": "Lead Platform Developer @ Adverts.ie",
        "Nerijus Urbietis": "Junior Desktop Support Engineer",
        "Noel Tate": "Marketplaces Product",
        "Padraig Howlin": "Head of Engineering - Property and Motor",
        "Paul Harrington": "Product, Motor",
        "Paula Tierney": "Motor Customer Support @DoneDeal.ie",
        "Peter Burrows": "Engineering Manager - SRE",
        "Priyanka Sonkar": "",
        "Renata Marini": "Finance Administrator",
        "Rob Hume": "Motor - Strategy & Business Development",
        "Roisin": "Customer Support Representative",
        "Ronan Doyle": "Senior Android Developer",
        "Ronan O Keeffe": "Site Reliability Engineer @ Daft and DoneDeal",
        "Ronan O'Neill": "Head of Engineering",
        "Sarah Downey": "",
        "Sean Culleton": "Interim Engineering Manager - Quality",
        "Sean Reddin": "Business Development Executive",
        "Sergio Bestetti": "IT Support",
        "Shane Fox": "Engineering Manager  - Platform",
        "Simon Andreucetti": "Strategic Account \u200bDirector | Motor Division",
        "Stephen O'Neill": "Product Owner",
        "Stephen O'Reilly": "Customer Service Advisor",
        "apollo-bot": "Posts messages/images to apollo-log channel",
        "superscouse": "Tout and Scammer hunter at Adverts.ie"
    }
    round_msg = render_template('job', person=person, job=people[person])
    return statement(round_msg)


if __name__ == '__main__':
    app.run(debug=True)
