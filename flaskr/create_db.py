#!/usr/bin/python3

import os
from kleros_db_schema import db, Dispute
from kleros import Kleros, KlerosDispute, KlerosVote

kleros = Kleros(os.environ["ETH_NODE_URL"])
dispute_id = 0

db.drop_all()
db.create_all()

for dispute_id in range(0,10):
    try:
        kleros_dispute = kleros.dispute(dispute_id)
    except ValueError:
        break
    print("Creating %s" % dispute_id)
    kleros_dispute.get_creation_event()
    d = Dispute(
        id = dispute_id,
        created_by = kleros_dispute.address,
        created_date = kleros_dispute.creation_date,
        created_tx = kleros_dispute.txid

#        subcourt_id = kleros_dispute.sub_court_id,
#        tokens_at_stake_per_juror = kleros_dispute.get_PNK_at_stake() / 10 ** 18
    )
    db.session.add(d)

    appeal_id = 0
    #dispute_id += 1

db.session.commit()
