#!/usr/bin/python3

import sys
sys.path.extend(('lib', 'db'))

from kleros_db_schema import db, Dispute
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kleros.db'
db = SQLAlchemy(app)

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

@app.route('/', methods=['GET'])
def disputes():
    disputes = Dispute.query.all()

    return render_template('monitor/disputes.html', disputes=disputes)
