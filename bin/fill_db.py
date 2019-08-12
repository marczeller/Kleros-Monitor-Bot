#!/usr/bin/python3

import getopt
import sys
from datetime import datetime
from time import gmtime, strftime
sys.path.extend(('lib', 'db'))

import os
from kleros import db, Dispute, Round, Vote, Config, Court, JurorStake
from kleros_eth import KlerosEth
from makerdao_medianizer import MakerDAO_Medianizer

kleros_eth = KlerosEth(os.environ["ETH_NODE_URL"])
makerdao_medianizer = MakerDAO_Medianizer(os.environ["ETH_NODE_URL"])
config = Config()

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
    db.session.add(Court( id = 1, name = "Court 1"))
    db.session.add(Court( id = 2, name = "TCR Court"))
    db.session.add(Court( id = 3, name = "Ethfinex Court"))
    db.session.add(Court( id = 4, name = "ERC20 Court"))
    config.set('dispute_search_block', KlerosEth.initial_block)
    config.set('staking_search_block', KlerosEth.initial_block)
    db.session.commit()

for opt, arg in opts:
    if opt in ('-r', '--rebuild'):
        rebuild_db()

print("Fetching ETH price in USD")
eth_price = makerdao_medianizer.eth_price()
config.set('eth_price', eth_price)
print("ETH price is : %s USD" % eth_price)

print("Fetching disputes from block %s" % config.get('dispute_search_block'))

found_open_dispute = False

for dispute_eth in kleros_eth.dispute_events(config.get('dispute_search_block')):
    dispute = Dispute.query.get(dispute_eth['dispute_id'])
    if dispute != None:
        if dispute.ruled: continue
        dispute.delete_recursive()

    dispute_eth.update(kleros_eth.dispute_data(dispute_eth['dispute_id']))

    if (not found_open_dispute) and (not dispute_eth['ruled']):
        found_open_dispute = True
        config.set('dispute_search_block', dispute_eth['block_number'] - 1)

    print("Creating dispute %s" % dispute_eth['dispute_id'])

    dispute = Dispute(
        id = dispute_eth['dispute_id'],
        created_by = dispute_eth['creator'],
        created_date = dispute_eth['date'],
        created_tx = dispute_eth['txid'],
        ruled = dispute_eth['ruled'],
        subcourt_id = dispute_eth['subcourt_id'],
        current_ruling = dispute_eth['ruling'],
        period = dispute_eth['period'],
        last_period_change = datetime.fromtimestamp(dispute_eth['last_period_change']),
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

print("Fetching stakings from block %s" % config.get('staking_search_block'))

for staking_eth in kleros_eth.staking_events(config.get('staking_search_block')):
    print("Adding staking in block %s" % staking_eth['block_number'])
    staking = JurorStake(
        address = staking_eth['address'],
        court_id = staking_eth['court_id'],
        staking_date = staking_eth['date'],
        staking_amount = staking_eth['staked'],
        txid = staking_eth['txid']
    )
    db.session.add(staking)

    config.set('staking_search_block', staking_eth['block_number'] + 1)

config.set('updated', strftime("%Y-%m-%d %H:%M:%S", gmtime()))
