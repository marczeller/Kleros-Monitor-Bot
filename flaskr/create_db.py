#!/usr/bin/python3

import os
from kleros_db_schema import db, Dispute
from kleros import Kleros, KlerosDispute, KlerosVote

kleros = Kleros(os.environ["ETH_NODE_URL"])
dispute_id = 0

db.drop_all()
db.create_all()

while(True):
    try:
        kleros_dispute = KlerosDispute(dispute_id, kleros=kleros)
    except ValueError:
        break
    print("Creating %s" % dispute_id)
    d = Dispute(
        id = dispute_id
#        subcourt_id = kleros_dispute.sub_court_id,
#        tokens_at_stake_per_juror = kleros_dispute.get_PNK_at_stake() / 10 ** 18
    )
    db.session.add(d)

    appeal_id = 0

    

    dispute_id += 1

db.session.commit()
