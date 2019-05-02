#!/usr/bin/python3

import sys
import os
from kleros import Kleros, KlerosDispute, KlerosVote
from collections import Counter, defaultdict
import pprint

node_url = os.environ["ETH_NODE_URL"]

pp = pprint.PrettyPrinter(indent=2)
case_Number = 1
juror_accounts = []
while case_Number < 63:
    dispute = KlerosDispute(case_Number, node_url=node_url)
    appeal = len(dispute.rounds) - 1
    jurors = dispute.rounds[-1]

    for i in range(jurors):
    	Votingdata = KlerosVote(case_Number, node_url=node_url, appeal = appeal, vote_id = i)
    	dude_to_add = Votingdata.account
    	juror_accounts.append(dude_to_add)        
    case_Number = case_Number + 1

unique_jurors = dict(Counter(juror_accounts))
new_unique_jurors = defaultdict(list)
{new_unique_jurors[v].append(k) for k, v in unique_jurors.items()}

dispute_number = case_Number - 1
print("A total of %s unique jurors have been picked on Kleros" % len(unique_jurors))
print("A total of %s disputes have been arbitraged on Kleros" % dispute_number)
pp.pprint(new_unique_jurors)
