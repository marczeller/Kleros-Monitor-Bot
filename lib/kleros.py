#!/usr/bin/python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

import statistics

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db/kleros.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Config(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    option = db.Column(db.String)
    value = db.Column(db.String)

    @classmethod
    def get(cls, db_key):
        query = cls.query.filter(cls.option == db_key).first()
        if query == None: return None
        return query.value

    @classmethod
    def set(cls, db_key, db_val):
        query = cls.query.filter(cls.option == db_key)
        for item in query: db.session.delete(item)
        db.session.commit()
        new_option = cls(option = db_key, value = db_val)
        db.session.add(new_option)
        db.session.commit()

class Court(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    parent = db.Column(db.Integer, db.ForeignKey("court.id"), nullable=True)

    def disputes(self):
        return Dispute.query.filter(Dispute.subcourt_id == self.id).order_by(Dispute.id.desc())

    def children_ids(self):
        children_ids = []
        children = Court.query.filter(Court.parent == self.id)
        for child in children:
            children_ids.append(child.id)
            for grand_child in child.children_ids():
                children_ids.append(grand_child)
        return children_ids

    @property
    def jurors(self):

        jurors_query = db.session.execute(
            "SELECT DISTINCT(account) as address, count(vote.id) from vote, round, dispute \
            WHERE dispute.subcourt_id = :court_id \
            AND vote.round_id = round.id \
            AND round.dispute_id = dispute.id \
            GROUP BY address",
            {'court_id': self.id}
        )
        jurors = []
        for jq in jurors_query:
            jurors.append(Juror(jq[0]))
        return jurors

    def jurors_stakings(self):
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
        for juror in self.jurors_stakings(): amounts.append(juror['staking_amount'])
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

    def rounds(self):
        return Round.query.filter_by(dispute_id = self.id).all()

    @property
    def court(self):
        return Court.query.get(self.subcourt_id)

    @property
    def period_name(self):
        period_name = {
            0 : "Evidence",
            1 : "Commit",
            2 : "Vote",
            3 : "Appeal",
            4 : "Execution",
        }
        return period_name[self.period]

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

    def votes(self):
        return Vote.query.filter_by(round_id = self.id).all()

    def delete_recursive(self):
        votes = Vote.query.filter(Vote.round_id == self.id)
        for v in votes:
            print("Deleting vote %s" % v.id)
            db.session.delete(v)
        print("Deleting round %s" % self.id)
        db.session.delete(self)
        db.session.commit()

    @property
    def majority_reached(self):
        votes_cast = Vote.query.filter(Vote.round_id == self.id).filter(Vote.vote == 1).count()
        return votes_cast * 2 >= self.draws_in_round

    @property
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

    @property
    def is_winner(self):
        round = Round.query.get(self.round_id)
        if not round.majority_reached: return False
        return self.choice == round.winning_choice

class Juror():
    def __init__(self, address):
        self.address = address

    @classmethod
    def list(cls):
        jurors_query = db.session.execute(
            "SELECT DISTINCT(vote.account), count(vote.id) from vote, round, dispute \
            WHERE vote.round_id = round.id \
            AND round.dispute_id = dispute.id \
            GROUP BY vote.account"
        )
        jurors = []
        for jq in jurors_query:
            jurors.append({
                'address':jq[0],
                'votes': jq[1]
            })
        return jurors

    @property
    def stakings(self):
        stakings_query = JurorStake.query.filter(JurorStake.address == self.address).order_by(JurorStake.staking_date.desc())
        stakings = []
        for staking in stakings_query:
            stakings.append(staking)
        return stakings

    @property
    def current_stakings_per_court(self):
        stakings_query = db.session.execute(
            "SELECT MAX(id), court_id FROM juror_stake \
            WHERE address = :address \
            group by court_id", {'address': self.address }
        )
        stakings = {}
        for sq in stakings_query:
            stakings[sq[1]] = JurorStake.query.get(sq[0])
        return stakings

    @property
    def current_amounts_per_court(self):
        stakings = self.current_stakings_per_court
        amounts = {}
        for court_id in stakings:
            court = Court.query.get(court_id)
            if court == None: continue
            record = {'court_only': stakings[court_id].staking_amount}
            staking_with_children = stakings[court_id].staking_amount
            for p in court.children_ids():
                if p in stakings:
                    staking_with_children += stakings[p].staking_amount
            record['court_and_children'] = staking_with_children
            amounts[court_id] = record
        return amounts

class JurorStake(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String)
    court_id = db.Column(db.Integer, db.ForeignKey("court.id"), nullable=False)
    staking_date = db.Column(db.DateTime)
    staking_amount = db.Column(db.Float)
    txid = db.Column(db.String)

class Deposit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String)
    cdate = db.Column(db.DateTime)
    amount = db.Column(db.Float)
    txid = db.Column(db.String)
    court_id = db.Column(db.Integer, db.ForeignKey("court.id"), nullable=False)
    token_contract = db.Column(db.String) # FIXME

    @classmethod
    def total(cls):
        return cls.query.with_entities(func.sum(cls.amount)).all()[0][0]
