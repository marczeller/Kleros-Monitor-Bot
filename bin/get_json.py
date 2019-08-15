#!/usr/bin/python3

import sys
sys.path.extend(('lib', 'db'))

from kleros import db, Dispute, Round, Vote, Config, Court, JurorStake, Deposit

eth_price = float(Config.get('eth_price'))
round_price = round(eth_price, 2)
total_ETH = Deposit.total()
round_eth = round(total_ETH, 2)
total_USD = total_ETH * eth_price
round_total = round(total_USD, 2)

print("total_ETH deposited : %.2f ETH" % round_eth)
print("eth_price is %.2f USD" % round_price)
print(type(round_price))
print("total_USD deposited %.5f USD" % round_total)
