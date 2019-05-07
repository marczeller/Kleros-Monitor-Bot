import pytest
import os
from web3 import Web3, HTTPProvider

from kleros import Kleros, KlerosDispute, KlerosVote, KlerosDisputeRound

class TestKleros(object):
    kleros = Kleros(os.environ["ETH_NODE_URL"])
    disputes = {}
    for i in (16, 17, 42, 45, 52, 60):
        disputes[i] = KlerosDispute(i, contract = kleros.contract)

    def test_connection(self):
        assert type(self.kleros) is Kleros
        assert type(self.kleros.contract).__name__ == 'Contract'

    def test_dispute_rounds(self):
        assert type(self.disputes[16]) is KlerosDispute

    def test_ruling(self):
        assert self.disputes[16].current_ruling() == 2
        assert self.disputes[45].current_ruling() == 1

    def test_closed_dispute(self):
        assert self.disputes[16].dispute_status() == 2

    def test_pending_votes(self):
        assert len(self.disputes[17].rounds) == 3
        assert self.disputes[42].last_round.pending_votes() == 0
        assert self.disputes[17].last_round.pending_votes() == 3

    def test_define_losers(self):
    	assert self.disputes[17].last_round.losers() == 4
    	assert self.disputes[52].last_round.losers() == 0

    def test_define_win(self):
    	assert self.disputes[17].winning_choice() == 2
    	assert self.disputes[45].winning_choice() == 1
    	assert self.disputes[60].winning_choice() == 2

    def test_ETH_per_juror(self):
    	assert self.disputes[17].last_round.get_ETH_per_juror() == 0.55

    def test_PNK_per_juror(self):
    	assert self.disputes[17].last_round.tokens_at_stake_per_juror == 40000
