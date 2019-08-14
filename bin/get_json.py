#!/usr/bin/python3

#TO DO convert me into a lib class and connect that into fill_db.py
import sys
sys.path.extend(('lib', 'db'))
import os
import requests
from makerdao_medianizer import MakerDAO_Medianizer
makerdao_medianizer = MakerDAO_Medianizer(os.environ["ETH_NODE_URL"])
eth_price = makerdao_medianizer.eth_price()

address = '0x916deaB80DFbc7030277047cD18B233B3CE5b4Ab'
url = "https://api.etherscan.io/api?module=account&action=txlist&address=0x916deaB80DFbc7030277047cD18B233B3CE5b4Ab&startblock=7303699&endblock=99999999&sort=asc&apikey=GAN3HIU7QHKSP27MGXJPAAXUXEKVCU8C4X"
response = requests.get(url)
get_json = response.json()
result = get_json['result']
value_dump = []
result_len = len(result)
for i in range(0,result_len):
	from_address = get_json['result'][i]['from']
	if from_address != address:
		value_check = get_json['result'][i]['value']
		if value_check != '0':
			value_dump.append(int(value_check))

val_len = len(value_dump)
total = sum(value_dump)

total_ETH = total / 10 ** 18
total_USD = total_ETH * eth_price

print("total_ETH deposited : %.2f ETH" % total_ETH)
print("eth_price is %.2f USD" % eth_price)
print("total_USD deposited %.2f USD" % total_USD)
