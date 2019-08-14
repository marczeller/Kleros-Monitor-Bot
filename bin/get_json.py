#!/usr/bin/python3

import sys
sys.path.extend(('lib', 'db'))

from kleros import db, Dispute, Round, Vote, Config, Court, JurorStake, Deposit

eth_price = float(Config.get('eth_price'))
total_ETH = Deposit.total()
total_USD = total_ETH * eth_price

print("total_ETH deposited : %.2f ETH" % total_ETH)
print("eth_price is %.2f USD" % eth_price)
print("total_USD deposited %.2f USD" % total_USD)
