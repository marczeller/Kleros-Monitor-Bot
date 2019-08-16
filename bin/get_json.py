#!/usr/bin/python3

import sys
sys.path.extend(('lib', 'db'))

from kleros import db, Dispute, Round, Vote, Config, Court, JurorStake, Deposit, Juror

eth_price = float(Config.get('eth_price'))
round_price = round(eth_price, 2)
total_ETH = Deposit.total()
round_eth = round(total_ETH, 2)
total_USD = total_ETH * eth_price
round_total = round(total_USD, 2)


#print(j)
#print(len(j))
total_jurors = 0
total_votes = 0
for court in range(5):
	c = Court.query.get(court)
	j = c.jurors
	total_jurors += len(j)
	for vote in range(len(j)):
		votes = j[vote]['votes']
		total_votes += votes
#print(len(j))
#print(total_jurors)
#print("total_ETH deposited : %.2f ETH" % round_eth)
#print("eth_price is %.2f USD" % round_price)
#print("total_USD deposited %.5f USD" % round_total)

a = Juror.list()
print(a)
print(len(a))
