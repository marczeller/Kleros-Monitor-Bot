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
