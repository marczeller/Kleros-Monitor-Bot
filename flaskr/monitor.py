#!/usr/bin/python3

import sys
sys.path.extend(('lib', 'db'))

from kleros_db_schema import db, Dispute, Round, Vote
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kleros.db'
db = SQLAlchemy(app)

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

@app.route('/disputes', methods=['GET'])
def disputes():
    disputes = Dispute.query.all()

    return render_template('monitor/disputes.html', disputes=disputes)

@app.route('/dispute/<int:id>', methods=['GET'])
def dispute(id):
    dispute = Dispute.query.get(id)
    rounds = Round.query.filter_by(dispute_id = id).all()
    votes = []
    for r in rounds:
        r.votes = Vote.query.filter_by(round_id = r.id).all()
        for v in r.votes:
            if v.choice == 2: v.vote_str = 'Yes'
            elif v.choice == 1: v.vote_str = 'No'
            else: v.vote_str = 'Pending'

            if r.majority_reached:
                if v.choice == 0: v.color = '#F7DC6F'
                elif v.choice == r.winning_choice: v.color = '#27AE60'
                else: v.color = '#E74C3C'
            else:
                if v.choice == 0: v.color = '#FCF3CF'
                elif v.choice == r.winning_choice: v.color = '#D1F2EB'
                else: v.color = '#F5B7B1'

    x = len(rounds)
    return render_template('monitor/dispute.html', dispute=dispute, rounds=rounds, x=x)


# d = Dispute.query.get(17)
# r = Round.query.filter(Round.dispute_id == d.id).all()
# r2 = r[2]
# v = Vote.query.filter(Vote.round_id == r2.id).all()
