#!/usr/bin/python3

import sys
sys.path.extend(('lib', 'db'))

from kleros import db, Dispute, Round, Vote, Config, Court, JurorStake, Deposit, Juror
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from datetime import datetime
from time import gmtime, strftime

import statistics

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db/kleros.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

@app.route('/court/<int:id>', methods=['GET'])
def court(id):
    court = Court.query.get(id)
    court.disputes = court.disputes()

    staking_data = []
    for juror in court.jurors:
        juror_data = juror.current_amount_in_court(court.id)
        votes_in_court = juror.votes_in_court(court.id)
        if juror_data['court_and_children'] == 0 and votes_in_court == 0: continue
        staking_data.append({
            'address': juror.address,
            'votes_in_court': votes_in_court,
            'court_only': juror_data['court_only'],
            'court_and_children': juror_data['court_and_children']
        })

    court.staking_data = sorted(staking_data,
        key=lambda x: (x['court_and_children'], x['votes_in_court']), reverse=True)
    num_Jurors = len(court.jurors) - 1

    return render_template('monitor/court.html',
        court=court,
        last_updated=Config.get('updated'),
        num_Jurors=num_Jurors,
        jurors_stats=[], full_jurors=[], full_jurors_stats=[], voting_jurors_num=[]
    )

'''
    court_num = court
    voting_jurors = court_num.jurors
    voting_jurors_num = len(voting_jurors)
    jurors = court.jurors_stakings()
    jurors_stats = court.juror_stats()


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
        for c in courts:
            court_jurors = c.jurors_stakings()
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

    return render_template('monitor/court.html', court=court, disputes=disputes, jurors=jurors, last_updated=Config.get('updated'),
        jurors_stats=jurors_stats, full_jurors=full_jurors, full_jurors_stats=full_jurors_stats, voting_jurors_num=voting_jurors_num)
'''



@app.route('/', methods=['GET'])
@app.route('/disputes', methods=['GET'])

def disputes():
    disputes = Dispute.query.order_by(Dispute.id.desc()).all()
    total_ETH = Deposit.total()
    round_eth = round(total_ETH, 2)
    eth_price = float(Config.get('eth_price'))
    round_price = round(eth_price, 2)
    total_in_USD = round(round_eth * round_price, 2)
    unique_voting_jurors = Juror.list()
    return render_template('monitor/disputes.html', disputes=disputes, last_updated=Config.get('updated'), round_eth=round_eth, round_price=round_price, total_in_USD=total_in_USD, voting_jurors=len(unique_voting_jurors))

@app.route('/dispute/<int:id>', methods=['GET'])
def dispute(id):
    dispute = Dispute.query.get(id)
    dispute.rounds = dispute.rounds()
    for r in dispute.rounds:
        r.votes = r.votes()
        for v in r.votes:
            if v.choice == 1: v.vote_str = 'Yes'
            elif v.choice == 2: v.vote_str = 'No'
            else: v.vote_str = 'Pending'

            if r.majority_reached:
                if v.choice == 0: v.color = '#F7DC6F'
                elif v.choice == r.winning_choice: v.color = '#27AE60'
                else: v.color = '#E74C3C'
            else:
                if v.choice == 0: v.color = '#FCF3CF'
                elif v.choice == r.winning_choice: v.color = '#D1F2EB'
                else: v.color = '#F5B7B1'

    return render_template('monitor/dispute.html',
        dispute=dispute,
        last_updated=Config.get('updated')
    )

@app.route('/juror/<string:address>', methods=['GET'])
def juror(address):

    votes = (db.session.query(Vote, Round)
        .filter(func.lower(Vote.account) == address.lower())
        .filter(Vote.round_id == Round.id)
        .order_by(Vote.round_id.desc())
        .all()
    )

    for v in votes:
        if v[0].vote == 0: v[0].color = '#F7DC6F'
        else:
            if v[0].is_winner: v[0].color = '#27AE60'
            else: v[0].color = '#F5B7B1'

    stakes = (db.session.query(JurorStake, Court)
        .filter(func.lower(JurorStake.address) == address.lower())
        .filter(Court.id == JurorStake.court_id)
        .order_by(JurorStake.staking_date.desc())
        .all())

    disputes = Dispute.query.filter(func.lower(Dispute.created_by) == address.lower()).order_by(Dispute.created_date.desc())

    return render_template('monitor/juror.html', address=address, votes=votes, stakes = stakes, disputes=disputes, last_updated=Config.get('updated'))
