#!/usr/bin/python3

import getopt
import sys
from datetime import datetime
sys.path.extend(('lib', 'db'))

import os
from kleros import db, Dispute, Round, Vote, Kleroscan, Court, JurorStake
from kleros_eth import KlerosEth

kleros_eth = KlerosEth(os.environ["ETH_NODE_URL"])

try:
    opts, args = getopt.getopt(sys.argv[1:], "r", ["rebuild"])
except getopt.GetoptError as err:
    print(err) # will print something like "option -a not recognized"
    usage()
    sys.exit(2)

def rebuild_db():
    db.drop_all()
    db.create_all()
    db.session.add(Court( id = 0, name = "General Court"))
    db.session.add(Court( id = 2, name = "TCR Court"))
    db.session.add(Court( id = 3, name = "Ethfinex Court"))
    db.session.add(Court( id = 4, name = "ERC20 Court"))
    db.session.commit()

for opt, arg in opts:
    if opt in ('-r', '--rebuild'):
        rebuild_db()

for dispute_eth in kleros_eth.dispute_events():
    dispute = Dispute.query.get(dispute_eth['dispute_id'])
    if dispute.ruled: continue

    dispute_eth.update(kleros_eth.dispute_data(dispute_eth['dispute_id']))

    dispute.delete_recursive()

    dispute = Dispute(
        id = dispute_eth['dispute_id'],
        created_by = dispute_eth['creator'],
        created_date = dispute_eth['date'],
        created_tx = dispute_eth['txid'],
        ruled = dispute_eth['ruled'],
        subcourt_id = dispute_eth['subcourt_id'],
        current_ruling = dispute_eth['ruling']
    )

    db.session.add(dispute)
    db.session.commit()

    rounds = kleros_eth.dispute_rounds(dispute_eth['dispute_id'])

    for round_num in range(0, len(rounds)):
        round_eth = rounds[round_num]

        round = Round(
            dispute_id = dispute_eth['dispute_id'],
            round_num = round_num,
            draws_in_round = round_eth['jury_size'],
            tokens_at_stake_per_juror = round_eth['tokens_at_stake_per_juror'],
            total_fees_for_jurors = round_eth['total_fees'],
            commits_in_round = round_eth['votes'],
            repartitions_in_each_round = round_eth['repartition'],
            penalties_in_each_round = round_eth['penalties']
        )

        db.session.add(round)
        db.session.commit()

        for vote_num in range(0, round.draws_in_round):
            vote_eth = kleros_eth.vote(dispute_eth['dispute_id'], round_num, vote_num)

            vote = Vote(
                round_id = round.id,
                account = vote_eth['address'],
                commit = vote_eth['commit'],
                choice = vote_eth['choice'],
                vote = vote_eth['vote']
            )

            db.session.add(vote)
        db.session.commit()



'''

while(True):

    dispute = Dispute.query.get(dispute_id)
    if dispute != None:
        if dispute.ruled:
            dispute_id += 1
            continue
        else:
            dispute.delete_recursive()
    try:
        dispute_eth = kleros_eth.

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

last_block = get_db_option('last_block') or kleros.initial_block
print("Retrieving juror stakes, starting at block %s" % last_block)
kleros.get_juror_stakes()
print ("Done")

for stake in kleros.juror_stakes:
    s = JurorStake(
        address = stake['address'],
        court_id = stake['court_id'],
        staking_amount = stake['amount'] / 10**18,
        staking_date = stake['date']
    )
    db.session.add(s)
    last_block = stake['block']

set_db_option('last_block', last_block)
set_db_option('last_updated', datetime.utcnow())

'''
