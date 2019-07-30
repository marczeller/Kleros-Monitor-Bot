#!/usr/bin/python3

import sys
sys.path.extend(('lib', 'db'))

from kleros import db, Dispute, Round, Vote, Config, Court, JurorStake
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

import statistics

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kleros.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
config = Config()

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

@app.route('/court/<int:id>', methods=['GET'])
def court(id):
    court = Court.query.get(id)
    disputes = Dispute.query.filter(Dispute.subcourt_id == id).order_by(Dispute.id.desc())
    jurors = court.jurors()
    jurors_stats = court.juror_stats()

    court_name = {
    0 : "General Court",
    1 : "Null",
    2 : "TCR Court",
    3 : "Ethfinex Court",
    4 : "ERC20 Court",
    }

    court_mapping = {
        0: [2, 3, 4],
        2: [3, 4,]
    }
    full_jurors = []
    full_jurors_stats = {}
    if id in court_mapping:
        amounts = []
        unique_jurors = {}
        for j in jurors:
            if j['address'] not in unique_jurors:
                unique_jurors[j['address']] = {"staking_amount": j['staking_amount']}
            else:
                unique_jurors[j['address']]["staking_amount"] += j['staking_amount']
            amounts.append(j['staking_amount'])

        courts = Court.query.filter(Court.id.in_(court_mapping[id]))
        for court in courts:
            court_jurors = court.jurors()
            for cj in court_jurors:
                if cj['address'] not in unique_jurors:
                    unique_jurors[cj['address']] = {"staking_amount": cj['staking_amount']}
                else:
                    unique_jurors[cj['address']]["staking_amount"] += cj['staking_amount']
                amounts.append(cj['staking_amount'])

        full_jurors_stats['length'] = len(amounts)
        full_jurors_stats['mean'] = statistics.mean(amounts)
        full_jurors_stats['median'] = statistics.median(amounts)
        full_jurors = [{'address': address, 'staking_amount': juror['staking_amount']} for address, juror in unique_jurors.items()]
        full_jurors = sorted(full_jurors, key=lambda j: j['staking_amount'], reverse=True)

    return render_template('monitor/court.html', court=court, disputes=disputes, jurors=jurors, last_updated=config.get('updated'),
        jurors_stats=jurors_stats, full_jurors=full_jurors, full_jurors_stats=full_jurors_stats, court_name=court_name[id])

@app.route('/', methods=['GET'])
@app.route('/disputes', methods=['GET'])
def disputes():
    disputes = Dispute.query.order_by(Dispute.id.desc()).all()
    for dispute in disputes:
        court = Court.query.get(dispute.subcourt_id)
        if court != None:
            dispute.court_name = court.name
        else:
            dispute.court_name = "Court #%" % dispute.subcourt_id

    return render_template('monitor/disputes.html', disputes=disputes, last_updated=config.get('updated'))

@app.route('/dispute/<int:id>', methods=['GET'])
def dispute(id):
    dispute = Dispute.query.get(id)
    rounds = Round.query.filter_by(dispute_id = id).all()
    votes = []
    for r in rounds:
        r.majority_reached = r.majority_reached()
        r.votes = Vote.query.filter_by(round_id = r.id).all()
        for v in r.votes:
            if v.choice == 1: v.vote_str = 'Yes'
            elif v.choice == 2: v.vote_str = 'No'
            else: v.vote_str = 'Pending'

            if r.majority_reached:
                if v.choice == 0: v.color = '#F7DC6F'
                elif v.choice == r.winning_choice(): v.color = '#27AE60'
                else: v.color = '#E74C3C'
            else:
                if v.choice == 0: v.color = '#FCF3CF'
                elif v.choice == r.winning_choice(): v.color = '#D1F2EB'
                else: v.color = '#F5B7B1'

    x = len(rounds)
    return render_template('monitor/dispute.html', dispute=dispute, rounds=rounds, x=x, last_updated=config.get('updated'))

@app.route('/juror/<string:address>', methods=['GET'])
def juror(address):

    address = address.lower()

    votes = Vote.query.filter(func.lower(Vote.account) == address).order_by(Vote.round_id.desc())
    stakes = JurorStake.query.filter(func.lower(JurorStake.address) == address).order_by(JurorStake.staking_date.desc())
    disputes = Dispute.query.filter(func.lower(Dispute.created_by) == address).order_by(Dispute.created_date.desc())

    return render_template('monitor/juror.html', address=address, votes=votes, stakes = stakes, disputes=disputes, last_updated=config.get('updated'))
