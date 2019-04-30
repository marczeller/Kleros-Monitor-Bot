#!/usr/bin/python3

import sys
import os
from kleros import Kleros, KlerosDispute, KlerosVote

node_url = os.environ["ETH_NODE_URL"]

# 'https://mainnet.infura.io/v3/31c378f901bf46c08674e655e6640287'

case_Number = int(sys.argv[1])
dispute = KlerosDispute(case_Number, node_url=node_url)
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
PNK_at_stake = dispute.get_PNK_at_stake()
ETH_at_Stake = dispute.get_ETH_at_stake()
PNK_per_juror = PNK_at_stake / jurors
ETH_per_juror = ETH_at_Stake / jurors
losers = dispute.define_losers()
choice = dispute.define_win_choice()

#TO DO MOVE winning_side() TO KLEROS.PY AS A METHOD OF KlerosVote

def winning_side():
    if votesYes > jurors // 2:
        losers = (votesNo + votesRefuse + pending_votes)
        win = "YES"
    elif votesNo > jurors // 2:
        losers = (votesYes + votesRefuse + pending_votes)
        win = "NO"
    elif votesRefuse > jurors // 2:
        losers = (votesNo + votesYes + pending_votes)
        win = "Refuse to Arbitrate"    
    else:
        print ("This case didn't reached consensus")
    ETH_distribution = ((losers * ETH_per_juror) / jurors) + ETH_per_juror
    PNK_distribution = (losers * PNK_per_juror) / (jurors - losers)
    print("Majority jurors who voted %s receive %.f PNK and %.3f ETH each" % (win, PNK_distribution, ETH_distribution))    

print("%s jurors drawn on last round" % jurors)
print("Each juror has staked %s PNK and might earn %.3f ETH on this case" % (PNK_per_juror, ETH_per_juror))
print("Yes votes: %s (%.2f %%)" % (votesYes, votesYes_ratio))
print("No votes : %s (%.2f %%)" % (votesNo, votesNo_ratio))
print("Refused to arbitrate : %s (%.2f %%)" % (votesRefuse, votesRefuse_ratio))

if pending_votes > 0:
    print("Pending votes: %s" % pending_votes)
else:
    print("Eveyone voted.")

if votesYes > votesNo:
    print("Outcome: Yes")
elif votesNo > votesYes:
    print("Outcome: No")
else:
    print("Outcome: Undecided")

if votesYes > jurors // 2 or votesNo > jurors // 2 or votesRefuse > jurors // 2:
    print("Absolute majority was reached")

    winning_side()

if case_closed_bool == True:
    print("The case is closed, a total of %s PNK was at stake and %.3f ETH was distributed to jurors" % (PNK_at_stake, ETH_at_Stake))
    
else:
	print("The case is still open, stay tuned for possible appeals")    