#!/usr/bin/python3

#TO DO convert me into a lib class and connect that into fill_db.py

import requests

address = '0x916deaB80DFbc7030277047cD18B233B3CE5b4Ab'
url = "https://api.etherscan.io/api?module=account&action=txlist&address=0x916deaB80DFbc7030277047cD18B233B3CE5b4Ab&startblock=7303699&endblock=99999999&sort=asc&apikey=GAN3HIU7QHKSP27MGXJPAAXUXEKVCU8C4X"
response = requests.get(url)
get_json = response.json()
result = get_json['result']
value_dump = []
result_len = len(result)
for i in range(0,result_len):
	temp = get_json['result'][i]['from']
	if temp == address:
		continue
	else:
		temp = get_json['result'][i]['value']
		if temp == '0':
			continue
		else:
			value_dump.append(int(temp))

val_len = len(value_dump)
total = 0
for i in range(0,val_len):
	total += value_dump[i]

print(total / 10 ** 18)
