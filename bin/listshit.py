#!/usr/bin/python3

import getopt
import sys
from datetime import datetime
sys.path.extend(('lib', 'db'))

import os
from kleros_db_schema import db, Dispute, Round, Vote, Kleroscan, Court
from kleros import Kleros, KlerosDispute, KlerosVote

k = Kleros(os.environ["ETH_NODE_URL"])

jurorlist = k.get_staking_jurors_list()
x = len(jurorlist)

y = k.get_staking_jurors_len()

z = k.get_staking_jurors_list()

a = k.get_juror_stakeOf()

f = k.get_len_stacking_dict()

b = k.get_staking_average()

print(b)