#!/usr/bin/python3

import getopt
import sys
from datetime import datetime
from time import gmtime, strftime

sys.path.extend(('lib', 'db'))

import os

from kleros import db, Dispute, Round, Vote, Config, Court, JurorStake, Deposit
from kleros_eth import KlerosEth
from makerdao_medianizer import MakerDAO_Medianizer
from etherscan import Etherscan

kleros_eth = KlerosEth(os.environ["ETH_NODE_URL"])
makerdao_medianizer = MakerDAO_Medianizer(os.environ["ETH_NODE_URL"])

try:
    opts, args = getopt.getopt(sys.argv[1:], "r", ["rebuild"])
except getopt.GetoptError as err:
    print(err) # will print something like "option -a not recognized"
    usage()
    sys.exit(2)

def rebuild_db():
    db.drop_all()
    db.create_all()
    db.session.add(Court( id = 0, name = "General Court", address = "0x0d67440946949fe293b45c52efd8a9b3d51e2522"))
    db.session.add(Court( id = 1, name = "Court 1", parent = 0, address = ""))
    db.session.add(Court( id = 2, parent = 0, name = "TCR Court", address = "0xebcf3bca271b26ae4b162ba560e243055af0e679"))
    db.session.add(Court( id = 3, parent = 2, name = "Ethfinex Court", address = "0x916deab80dfbc7030277047cd18b233b3ce5b4ab"))
    db.session.add(Court( id = 4, parent = 2, name = "ERC20 Court", address = "0xcb4aae35333193232421e86cd2e9b6c91f3b125f"))
    db.session.add(Court( id = 5, parent = 1, name = "", address = ""))
    db.session.add(Court( id = 6, parent = 1, name = "", address = ""))
    db.session.add(Court( id = 7, parent = 1, name = "", address = ""))
    Config.set('dispute_search_block', KlerosEth.initial_block)
    Config.set('staking_search_block', KlerosEth.initial_block)
    db.session.commit()

def create_dispute(dispute_eth):

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


for opt, arg in opts:
    if opt in ('-r', '--rebuild'):
        rebuild_db()

eth_price = makerdao_medianizer.eth_price()
Config.set('eth_price', eth_price) 
print("ETH price is : %s USD" % eth_price)

print("Fetching disputes from block %s" % Config.get('dispute_search_block'))

current_block = Config.get('dispute_search_block')
if (current_block) == None:
    current_block = 0
current_block = int(current_block)
end_block = int(kleros_eth.w3.eth.blockNumber)
found_open_dispute = False

while current_block < end_block:

    for dispute_eth in kleros_eth.dispute_events(current_block):
        dispute = Dispute.query.get(dispute_eth['dispute_id'])
        latest_dispute_block = dispute_eth['block_number']

        # Buggy case, will never get closed

        if dispute != None:
            if dispute.ruled: continue
            dispute.delete_recursive()

        dispute_eth.update(kleros_eth.dispute_data(dispute_eth['dispute_id']))
        create_dispute(dispute_eth)

        if int(dispute_eth['dispute_id']) not in (105,107,108): # Broken cases
            if(not dispute_eth['ruled']):
                found_open_dispute = True
    
    if (not found_open_dispute): 
        Config.set('dispute_search_block', current_block - 1)
    current_block += 100

print("Fetching stakings from block %s" % Config.get('staking_search_block'))

for staking_eth in kleros_eth.staking_events(Config.get('staking_search_block')):
    print("Adding staking in block %s" % staking_eth['block_number'])
    staking = JurorStake(
        address = staking_eth['address'],
        court_id = staking_eth['court_id'],
        staking_date = staking_eth['date'],
        staking_amount = staking_eth['staked'],
        txid = staking_eth['txid']
    )
    db.session.add(staking)

    Config.set('staking_search_block', staking_eth['block_number'] + 1)

print ("Fetching deposits")

Deposit.query.delete()

for court in Court.query.all():
    if court.address == "": continue
    print("Fetching deposits for %s" % court.name)
    for item in Etherscan.deposits(court.address):
        deposit = Deposit(
            address = item['from'],
            cdate = datetime.utcfromtimestamp(int(item['timeStamp'])),
            amount = int(item['value']) / 10**18,
            txid = item['hash'],
            token_contract = "XXX", # FIXME
            court_id = court.id
        )
        db.session.add(deposit)

db.session.commit()

Config.set('updated', strftime("%Y-%m-%d %H:%M:%S", gmtime()))
