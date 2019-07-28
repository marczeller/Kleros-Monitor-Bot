#!/usr/bin/python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import statistics

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db/kleros.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Config(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    option = db.Column(db.String)
    value = db.Column(db.String)

    def get(self, db_key):
        query = self.query.filter(self.__class__.option == db_key).first()
        if query == None: return None
        return query.value

    def set(self, db_key, db_val):
        query = self.query.filter(self.__class__.option == db_key)
        for item in query: db.session.delete(item)
        db.session.commit()
        new_option = self.__class__(option = db_key, value = db_val)
        db.session.add(new_option)
        db.session.commit()

class Court(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def jurors(self):
        jurors_query = db.session.execute(
            "SELECT address, staking_amount, MAX(staking_date) as 'date' \
            FROM juror_stake \
            WHERE court_id = :court_id \
            GROUP BY address \
            ORDER BY staking_amount DESC", {'court_id': self.id})

        jurors = []
        for jq in jurors_query:
            juror = dict(jq.items())
            if juror['staking_amount'] != 0: jurors.append(juror)

        return jurors

    def juror_stats(self):
        amounts = []
        for juror in self.jurors(): amounts.append(juror['staking_amount'])
        return {
            'length': len(amounts),
            'mean': statistics.mean(amounts),
            'median': statistics.median(amounts)
        }

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

    def delete_recursive(self):
        rounds = Round.query.filter(Round.dispute_id == self.id)
        for r in rounds: r.delete_recursive()
        print("Deleting Dispute %s" % self.id)
        db.session.delete(self)
        db.session.commit()

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

    def delete_recursive(self):
        votes = Vote.query.filter(Vote.round_id == self.id)
        for v in votes:
            print("Deleting vote %s" % v.id)
            db.session.delete(v)
        print("Deleting round %s" % self.id)
        db.session.delete(self)
        db.session.commit()

    def majority_reached(self):
        votes_cast = Vote.query.filter(Vote.round_id == self.id).filter(Vote.vote == 1).count()
        return votes_cast * 2 >= self.draws_in_round

    def winning_choice(self):
        votes = Vote.query.filter(Vote.round_id == self.id).count()
        votes_query = db.session.execute(
            "select choice,count(*) as num_votes from vote \
            where round_id = :round_id and vote=1 \
            group by choice order by num_votes desc", {'round_id': self.id}).first()
        return(votes_query[0])


class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    round_id = db.Column(db.Integer, db.ForeignKey("round.id"), nullable=False)
    account = db.Column(db.Integer)
    commit = db.Column(db.Integer)
    choice = db.Column(db.Integer)
    vote = db.Column(db.Integer)
    date = db.Column(db.DateTime)

class Juror(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String)

    def stakings(self):
        stakings_query = JurorStake.query.filter(JurorStake.address == self.address).order_by(JurorStake.staking_date.desc())
        stakings = []
        for staking in stakings_query:
            s = dict(staking.items())
            stakings.append(s)

        return stakings

class JurorStake(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String)
    court_id = db.Column(db.Integer, db.ForeignKey("court.id"), nullable=False)
    staking_date = db.Column(db.DateTime)
    staking_amount = db.Column(db.Float)
    txid = db.Column(db.String)
