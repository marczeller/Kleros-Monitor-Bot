import pytest
import os
from web3 import Web3, HTTPProvider

from kleros import Kleros, KlerosDispute, KlerosVote

class TestKleros(object):
    kleros = Kleros(os.environ["ETH_NODE_URL"])

    def test_connection(self):
        assert type(TestKleros.kleros) is Kleros
        assert type(TestKleros.kleros.connection).__name__ == 'Contract'

    def test_dispute_rounds(self):
        kleros_dispute = KlerosDispute(1, kleros = TestKleros.kleros)
        assert type(kleros_dispute) is KlerosDispute

    def test_ruling_no(self):
        kleros_dispute = KlerosDispute(16, kleros = TestKleros.kleros)
        assert kleros_dispute.current_ruling() == 2

    def test_ruling_yes(self):
        kleros_dispute = KlerosDispute(45, kleros = TestKleros.kleros)
        assert kleros_dispute.current_ruling() == 1

    def test_closed_dispute(self):
        kleros_dispute = KlerosDispute(16, kleros = TestKleros.kleros)
        assert kleros_dispute.dispute_status() == 2

    def test_open_dispute(self):
    	kleros_dispute = KlerosDispute(17, kleros = TestKleros.kleros)
    	assert kleros_dispute.dispute_status() == 1

    def test_pending_vote_zero(self):
    	kleros_dispute = KlerosDispute(42, kleros = TestKleros.kleros)
    	assert kleros_dispute.pending_vote() == 0

    def test_pending_votes(self):
    	kleros_dispute = KlerosDispute(17, kleros = TestKleros.kleros)
    	assert kleros_dispute.pending_vote() == 3

    def test_define_losers(self):
    	kleros_dispute = KlerosDispute(17, kleros = TestKleros.kleros)
    	assert kleros_dispute.define_losers() == 4

    def test_define_zero_losers(self):
    	kleros_dispute = KlerosDispute(52, kleros = TestKleros.kleros)
    	assert kleros_dispute.define_losers() == 0

    def test_define_no_win(self):
    	kleros_dispute = KlerosDispute(17, kleros = TestKleros.kleros)
    	assert kleros_dispute.define_win_choice() == "NO"

    def test_define_yes_win(self):
    	kleros_dispute = KlerosDispute(45, kleros = TestKleros.kleros)
    	assert kleros_dispute.define_win_choice() == "YES"	



