#!/usr/bin/python3

import sys
import os
from kleros import Kleros, KlerosDispute, KlerosVote
from collections import Counter, defaultdict
import pprint
import requests

case_Number = 0
node_url = os.environ["ETH_NODE_URL"]
kleros = Kleros(node_url)
pp = pprint.PrettyPrinter(indent=2)
juror_accounts = []
total_dispute = kleros.last_dispute_id()
print (total_dispute)

while case_Number <= total_dispute:
    dispute = KlerosDispute(case_Number, kleros=kleros)
    appeal = len(dispute.rounds) - 1
    jurors = dispute.rounds[-1]

    for i in range(jurors):
    	Votingdata = KlerosVote(case_Number, kleros=kleros, appeal = appeal, vote_id = i)
    	juror_accounts.append(Votingdata.account)
    case_Number = case_Number + 1

unique_jurors = dict(Counter(juror_accounts))
new_unique_jurors = defaultdict(list)
{new_unique_jurors[v].append(k) for k, v in unique_jurors.items()}
vote_counter = sum(unique_jurors.values())

print(new_unique_jurors)
print("A total of %s unique jurors have been picked on Kleros" % len(unique_jurors))
print("A total of %s disputes have been arbitraged on Kleros" % total_dispute)
print("Jurors have casted a total of %s votes" % (vote_counter))
