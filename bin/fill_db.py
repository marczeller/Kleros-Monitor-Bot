#!/usr/bin/python3

import getopt
import sys
from datetime import datetime
sys.path.extend(('lib', 'db'))

import os
from kleros_db_schema import db, Dispute, Round, Vote, Kleroscan, Court
from kleros import Kleros, KlerosDispute, KlerosVote

kleros = Kleros(os.environ["ETH_NODE_URL"])

try:
    opts, args = getopt.getopt(sys.argv[1:], "r", ["rebuild"])
except getopt.GetoptError as err:
    print(err) # will print something like "option -a not recognized"
    usage()
    sys.exit(2)

def rebuild_db():
    db.drop_all()
    db.create_all()
    court = Court( id = 0, name = "General Court")
    db.session.add(court)
    court = Court(id = 2, name = "TCR Court")
    db.session.add(court)
    court = Court(id = 3, name = "Ethfinex Court")
    db.session.add(court)
    court = Court(id = 4, name = "ERC20 Court")
    db.session.add(court)
    db.session.commit()

for opt, arg in opts:
    if opt in ('-r', '--rebuild'):
        rebuild_db()

def delete_dispute(dispute):
    rounds = Round.query.filter(Round.dispute_id == dispute.id)
    for r in rounds:
        votes = Vote.query.filter(Vote.round_id == r.id)
        for v in votes:
            print("Deleting vote %s" % v.id)
            db.session.delete(v)
        print("Deleting round %s" % r.id)
        db.session.delete(r)
    print("Deleting Dispute %s" % dispute.id)
    db.session.delete(dispute)
    db.session.commit()

dispute_id = 0

while(True):

    dispute = Dispute.query.get(dispute_id)
    if dispute != None:
        if dispute.ruled:
            dispute_id += 1
            continue
        else:
            delete_dispute(dispute)
    try:
        d = kleros.dispute(dispute_id)
    except ValueError:
        break

    print("Creating %s" % dispute_id)
    d.get_creation_event()

    dispute = Dispute(
        id = dispute_id,
        created_by = d.address,
        created_date = d.creation_date,
        created_tx = d.txid,
        ruled = d.ruled,
        subcourt_id = d.subcourt_id,
        current_ruling = d.current_ruling()

#        subcourt_id = kleros_dispute.sub_court_id,
#        tokens_at_stake_per_juror = kleros_dispute.get_PNK_at_stake() / 10 ** 18
    )

    db.session.add(dispute)

    for r in d.rounds:
        r.get_winning_choice()
        round = Round(
            dispute_id = dispute_id,
            round_num = r.round_id,
            draws_in_round = r.votes_length,
            tokens_at_stake_per_juror = r.tokens_at_stake_per_juror,
            total_fees_for_jurors = r.total_fees_for_jurors,
            commits_in_round = r.votes_count,
            repartitions_in_each_round = r.repartitions,
            penalties_in_each_round = r.penalties,
            winning_choice = r.winning_choice,
            majority_reached = r.majority_reached
        )
        db.session.add(round)
        db.session.commit()

        r.get_votes()

        for v in r.votes:
            vote_db = Vote(
                round_id = round.id,
                account = v.account,
                commit = v.commit,
                choice = v.choice,
                vote = v.vote
            )
            db.session.add(vote_db)
        db.session.commit()

    db.session.commit()

    appeal_id = 0
    dispute_id += 1

kleroscan = Kleroscan.query.filter(Kleroscan.option == 'last_updated')
for k in kleroscan:
    db.session.delete(k)
    db.session.commit()

kleroscan = Kleroscan(
    option = 'last_updated',
    value = datetime.utcnow()
)

db.session.add(kleroscan)
db.session.commit()
