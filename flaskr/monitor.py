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

    return render_template('monitor/dispute.html', dispute=dispute)


# d = Dispute.query.get(17)
# r = Round.query.filter(Round.dispute_id == d.id).all()
# r2 = r[2]
# v = Vote.query.filter(Vote.round_id == r2.id).all()
