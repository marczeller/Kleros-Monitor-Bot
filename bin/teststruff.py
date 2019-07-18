import sys
sys.path.extend(('lib', 'db'))

from kleros_db_schema import db, Dispute, Round, Vote, Kleroscan, Court
court = Court.query.get(2)
court.jurors()