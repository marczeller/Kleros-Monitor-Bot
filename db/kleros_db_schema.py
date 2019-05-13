#!/usr/bin/python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kleros.db'
db = SQLAlchemy(app)

class Dispute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_of_choices = db.Column(db.Integer)
    subcourt_id = db.Column(db.Integer)
    status = db.Column(db.Integer)
    arbitrated_address = db.Column(db.String)
    current_ruling = db.Column(db.Integer)
    period = db.Column(db.Integer)
    last_period_change = db.Column(db.Integer)
    ruled = db.Column(db.Boolean)
    created_by = db.Column(db.String)
    created_tx = db.Column(db.String)
    created_date = db.Column(db.DateTime)

class Round(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    round_num = db.Column(db.Integer)
    dispute_id = db.Column(db.Integer, db.ForeignKey("dispute.id"), nullable=False)
    draws_in_round = db.Column(db.Integer)
    commits_in_round = db.Column(db.Integer)
    appeal_start = db.Column(db.Integer)
    appeal_end = db.Column(db.Integer)
    vote_lengths = db.Column(db.Integer)
    tokens_at_stake_per_juror = db.Column(db.Integer)
    total_fees_for_jurors = db.Column(db.Integer)
    votes_in_each_round = db.Column(db.Integer)
    repartitions_in_each_round = db.Column(db.Integer)
    penalties_in_each_round = db.Column(db.Integer)

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    round_id = db.Column(db.Integer, db.ForeignKey("round.id"), nullable=False)
    account = db.Column(db.Integer)
    commit = db.Column(db.Integer)
    choice = db.Column(db.Integer)
    vote = db.Column(db.Integer)
    date = db.Column(db.DateTime)


class Jury(db.Model):
    id = db.Column(db.Integer, primary_key=True)
