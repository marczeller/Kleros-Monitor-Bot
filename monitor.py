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
pending_votes = jurors - votesYes - votesNo
case_state_bool = dispute.case_state()
subcourt_id = dispute.get_subcourt()
PNK_at_stake = dispute.get_PNK_at_stake()
ETH_at_Stake = dispute.get_ETH_at_stake() 

print("%s jurors drawn on last round" % jurors)
print("Yes votes: %s (%.2f %%)" % (votesYes, votesYes_ratio))
print("No votes : %s (%.2f %%)" % (votesNo, votesNo_ratio))

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

if votesYes > jurors // 2 or votesNo > jurors // 2:
    print("Absolute majority was reached")
else:
    print("Case is still undecided")
if case_state_bool == True:
  print("The case is closed, a total of %s PNK was at stake and %.3f ETH was distributed to jurors" % (PNK_at_stake, ETH_at_Stake))
else:
  print("The case is still open, %s PNK are at stake and %.3f ETH will be distributed to jurors" % (PNK_at_stake, ETH_at_Stake))

