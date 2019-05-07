#!/usr/bin/python3

import sys
import os
from kleros import Kleros, KlerosDispute, KlerosVote
from collections import Counter

node_url = os.environ["ETH_NODE_URL"]

kleros = Kleros(os.environ["ETH_NODE_URL"])

# 'https://mainnet.infura.io/v3/31c378f901bf46c08674e655e6640287'

case_Number = int(sys.argv[1])
dispute = KlerosDispute(case_Number, node_url=node_url)
appeal = len(dispute.rounds) - 1
jurors = dispute.rounds[-1]
votes = dispute.get_vote_counter()
votesYes = votes[1]
votesYes_ratio = (votesYes / jurors) * 100
votesNo = votes[2]
votesNo_ratio = (votesNo / jurors) * 100
votesRefuse = votes[0]
votesRefuse_ratio = (votesRefuse / jurors) * 100
pending_votes = dispute.pending_vote()
case_closed_bool = dispute.ruled
subcourt_id = dispute.sub_court_id
PNK_at_stake = dispute.get_PNK_at_stake() / 10 ** 18
ETH_at_Stake = dispute.get_ETH_at_stake() / 10 ** 18
PNK_per_juror = dispute.get_PNK_per_juror() / 10 ** 18
ETH_per_juror = dispute.get_ETH_per_juror() / 10 ** 18
losers = dispute.define_losers()
vote_choices = {
    0: 'Undecided',
    1: 'Yes',
    2: 'No'
}
winner = vote_choices[dispute.winning_choice()]

print("%s jurors drawn on last round \n" % jurors)
print("Each juror has staked %s PNK and might earn %.3f ETH on this case\n" % (PNK_per_juror, ETH_per_juror))
print("Yes votes: %s (%.2f %%)" % (votesYes, votesYes_ratio))
print("No votes : %s (%.2f %%)" % (votesNo, votesNo_ratio))
print("Refused to arbitrate : %s (%.2f %%)\n" % (votesRefuse, votesRefuse_ratio))

if pending_votes > 0:
    print("Pending votes: %s \n" % pending_votes)
else:
    print("Eveyone voted. \n")

print("Outcome: %s" % winner)

if votesYes > jurors // 2 or votesNo > jurors // 2 or votesRefuse > jurors // 2:
    # print("Absolute majority was reached")

#TO DO move this to Kleros.py
    ETH_distribution = ((losers * ETH_per_juror) / jurors) + ETH_per_juror
    PNK_distribution = (losers * PNK_per_juror) / (jurors - losers)
    print("Majority jurors who voted %s receive %.f PNK and %.3f ETH each \n" % (winner, PNK_distribution, ETH_distribution))
else:
    print("No earnings information available yet.\n")

if case_closed_bool == True:
    print("The case is closed, a total of %s PNK was at stake and %.3f ETH was distributed to jurors" % (PNK_at_stake, ETH_at_Stake))

else:
	print("The case is still open, stay tuned for possible appeals")

# TO DO move this to kleros.py

def get_account_list():
    juror_accounts = []
    for i in range(jurors):
        Votingdata = KlerosVote(case_Number, node_url=node_url, appeal = appeal, vote_id = i)
        juror_accounts.append(Votingdata.account)
    return juror_accounts

raw_account_list = get_account_list()

def get_sorted_list():
    unique_jurors = dict(Counter(raw_account_list))
    clean_list = []
    for i in unique_jurors:
        clean_list.append(i)
    return clean_list

unique_jurors = get_sorted_list()

def get_total_PNK_stake_juror():
    stake = []
    for i in range(len(unique_jurors)):
        x = dispute.get_juror_PNK_staked(account = unique_jurors[i], subcourtID = subcourt_id) / 10 ** 18
#dumb as fuck, we need something that iterate every court id until they find the juror stake on the same dispute some jurors can have staked in different subcourts.
        if x == 0:
            new_subcourt_id = subcourt_id + 1
            x = dispute.get_juror_PNK_staked(account = unique_jurors[i], subcourtID = new_subcourt_id) / 10 ** 18
        stake.append(x)
    total = 0
    for i in stake:
        total = total + i
    return total

total_stake = get_total_PNK_stake_juror()

print("Jurors of this case have staked a total of %.f PNK on Kleros" % (total_stake))
