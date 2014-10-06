#!/usr/bin/env python

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User_cond(db.Model):
    uuid = db.Column(db.String(40), primary_key=True, unique=True)
    trials = db.Column(db.String(80))

    def __init__(self, uuid, trials):
        self.uuid = uuid
        self.trials = ','.join(trials)

    def __repr__(self):
        return '<User_cond %s> %s' % (self.uuid, self.trials)

class Response(db.Model):
    # id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    uuid = db.Column(db.String(40), primary_key=True)
    trial_num = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(80))
    timestamp = db.Column(db.DateTime)

    def __init__(self, uuid, trial_num, answer, timestamp):
        self.uuid = uuid
        self.trial_num = trial_num
        self.answer = answer
        self.timestamp = timestamp

    def __repr__(self):
        return '<Response %s> %s' % (self.uuid, self.answer)