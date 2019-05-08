from web3 import Web3, HTTPProvider
from datetime import datetime

class Kleros:
    abi = '[{"constant":false,"inputs":[{"name":"_pinakion","type":"address"}],"name":"changePinakion","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"RNBlock","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"disputesWithoutJurors","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"passPhase","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"governor","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"lastDelayedSetStake","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_disputeID","type":"uint256"}],"name":"disputeStatus","outputs":[{"name":"status","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_disputeID","type":"uint256"}],"name":"passPeriod","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"maxDrawingTime","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_disputeID","type":"uint256"}],"name":"currentRuling","outputs":[{"name":"ruling","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"courts","outputs":[{"name":"parent","type":"uint96"},{"name":"hiddenVotes","type":"bool"},{"name":"minStake","type":"uint256"},{"name":"alpha","type":"uint256"},{"name":"feeForJuror","type":"uint256"},{"name":"jurorsForCourtJump","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_appeal","type":"uint256"},{"name":"_iterations","type":"uint256"}],"name":"execute","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"ALPHA_DIVISOR","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_voteIDs","type":"uint256[]"},{"name":"_choice","type":"uint256"},{"name":"_salt","type":"uint256"}],"name":"castVote","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_subcourtID","type":"uint96"},{"name":"_minStake","type":"uint256"}],"name":"changeSubcourtMinStake","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_subcourtID","type":"uint96"}],"name":"getSubcourt","outputs":[{"name":"children","type":"uint256[]"},{"name":"timesPerPeriod","type":"uint256[4]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"appeal","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"onTransfer","outputs":[{"name":"allowed","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"disputes","outputs":[{"name":"subcourtID","type":"uint96"},{"name":"arbitrated","type":"address"},{"name":"numberOfChoices","type":"uint256"},{"name":"period","type":"uint8"},{"name":"lastPeriodChange","type":"uint256"},{"name":"drawsInRound","type":"uint256"},{"name":"commitsInRound","type":"uint256"},{"name":"ruled","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_subcourtID","type":"uint96"},{"name":"_timesPerPeriod","type":"uint256[4]"}],"name":"changeSubcourtTimesPerPeriod","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_subcourtID","type":"uint96"},{"name":"_feeForJuror","type":"uint256"}],"name":"changeSubcourtJurorFee","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_subcourtID","type":"uint96"},{"name":"_alpha","type":"uint256"}],"name":"changeSubcourtAlpha","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_voteIDs","type":"uint256[]"},{"name":"_commit","type":"bytes32"}],"name":"castCommit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"RN","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"RNGenerator","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_destination","type":"address"},{"name":"_amount","type":"uint256"},{"name":"_data","type":"bytes"}],"name":"executeGovernorProposal","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_minStakingTime","type":"uint256"}],"name":"changeMinStakingTime","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"NON_PAYABLE_AMOUNT","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_subcourtID","type":"uint96"},{"name":"_stake","type":"uint128"}],"name":"setStake","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_disputeID","type":"uint256"}],"name":"executeRuling","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_appeal","type":"uint256"},{"name":"_voteID","type":"uint256"}],"name":"getVote","outputs":[{"name":"account","type":"address"},{"name":"commit","type":"bytes32"},{"name":"choice","type":"uint256"},{"name":"voted","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_RNGenerator","type":"address"}],"name":"changeRNGenerator","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_iterations","type":"uint256"}],"name":"executeDelayedSetStakes","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_account","type":"address"},{"name":"_subcourtID","type":"uint96"}],"name":"stakeOf","outputs":[{"name":"stake","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_subcourtID","type":"uint96"},{"name":"_jurorsForCourtJump","type":"uint256"}],"name":"changeSubcourtJurorsForJump","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_disputeID","type":"uint256"}],"name":"appealPeriod","outputs":[{"name":"start","type":"uint256"},{"name":"end","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"phase","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MAX_STAKE_PATHS","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"delayedSetStakes","outputs":[{"name":"account","type":"address"},{"name":"subcourtID","type":"uint96"},{"name":"stake","type":"uint128"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"lastPhaseChange","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"minStakingTime","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"nextDelayedSetStake","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_numberOfChoices","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"createDispute","outputs":[{"name":"disputeID","type":"uint256"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_iterations","type":"uint256"}],"name":"drawJurors","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_parent","type":"uint96"},{"name":"_hiddenVotes","type":"bool"},{"name":"_minStake","type":"uint256"},{"name":"_alpha","type":"uint256"},{"name":"_feeForJuror","type":"uint256"},{"name":"_jurorsForCourtJump","type":"uint256"},{"name":"_timesPerPeriod","type":"uint256[4]"},{"name":"_sortitionSumTreeK","type":"uint256"}],"name":"createSubcourt","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_account","type":"address"}],"name":"getJuror","outputs":[{"name":"subcourtIDs","type":"uint96[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"},{"name":"_amount","type":"uint256"}],"name":"onApprove","outputs":[{"name":"allowed","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"jurors","outputs":[{"name":"stakedTokens","type":"uint256"},{"name":"lockedTokens","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_maxDrawingTime","type":"uint256"}],"name":"changeMaxDrawingTime","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_disputeID","type":"uint256"}],"name":"getDispute","outputs":[{"name":"votesLengths","type":"uint256[]"},{"name":"tokensAtStakePerJuror","type":"uint256[]"},{"name":"totalFeesForJurors","type":"uint256[]"},{"name":"votesInEachRound","type":"uint256[]"},{"name":"repartitionsInEachRound","type":"uint256[]"},{"name":"penaltiesInEachRound","type":"uint256[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_appeal","type":"uint256"}],"name":"getVoteCounter","outputs":[{"name":"winningChoice","type":"uint256"},{"name":"counts","type":"uint256[]"},{"name":"tied","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_governor","type":"address"}],"name":"changeGovernor","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"MIN_JURORS","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"appealCost","outputs":[{"name":"cost","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_owner","type":"address"}],"name":"proxyPayment","outputs":[{"name":"allowed","type":"bool"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[],"name":"lockInsolventTransfers","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_extraData","type":"bytes"}],"name":"arbitrationCost","outputs":[{"name":"cost","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"pinakion","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"_governor","type":"address"},{"name":"_pinakion","type":"address"},{"name":"_RNGenerator","type":"address"},{"name":"_minStakingTime","type":"uint256"},{"name":"_maxDrawingTime","type":"uint256"},{"name":"_hiddenVotes","type":"bool"},{"name":"_minStake","type":"uint256"},{"name":"_alpha","type":"uint256"},{"name":"_feeForJuror","type":"uint256"},{"name":"_jurorsForCourtJump","type":"uint256"},{"name":"_timesPerPeriod","type":"uint256[4]"},{"name":"_sortitionSumTreeK","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_phase","type":"uint8"}],"name":"NewPhase","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_disputeID","type":"uint256"},{"indexed":false,"name":"_period","type":"uint8"}],"name":"NewPeriod","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_address","type":"address"},{"indexed":false,"name":"_subcourtID","type":"uint256"},{"indexed":false,"name":"_stake","type":"uint128"},{"indexed":false,"name":"_newTotalStake","type":"uint256"}],"name":"StakeSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_address","type":"address"},{"indexed":true,"name":"_disputeID","type":"uint256"},{"indexed":false,"name":"_appeal","type":"uint256"},{"indexed":false,"name":"_voteID","type":"uint256"}],"name":"Draw","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_address","type":"address"},{"indexed":true,"name":"_disputeID","type":"uint256"},{"indexed":false,"name":"_tokenAmount","type":"int256"},{"indexed":false,"name":"_ETHAmount","type":"int256"}],"name":"TokenAndETHShift","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_disputeID","type":"uint256"},{"indexed":true,"name":"_arbitrable","type":"address"}],"name":"DisputeCreation","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_disputeID","type":"uint256"},{"indexed":true,"name":"_arbitrable","type":"address"}],"name":"AppealPossible","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_disputeID","type":"uint256"},{"indexed":true,"name":"_arbitrable","type":"address"}],"name":"AppealDecision","type":"event"}]'

    kleros_address = '0x988b3A538b618C7A603e1c11Ab82Cd16dbE28069'
    initial_block = 7303699
    dispute_creation_event_topic = "0x141dfc18aa6a56fc816f44f0e9e2f1ebc92b15ab167770e17db5b084c10ed995"

    def __init__(self, node_url, kleros = None):
        if kleros == None:
            self.w3 = Web3(HTTPProvider(node_url)) #TODO Exceptions, errors
            self.contract = self.w3.eth.contract(
                address = Web3.toChecksumAddress(self.kleros_address),
                abi = self.abi
            )
        else:
            self.w3 = kleros.w3
            self.contract = kleros.contract

    def last_dispute_id(self):
        self.get_dispute_events()
        self.last_dispute_id = dispute_events[-1]['args']['_disputeID']
        return self.last_dispute_id

    def get_dispute_events(self):
        filter = self.contract.events.DisputeCreation.createFilter(fromBlock=self.initial_block,
            argument_filters={"topic0": self.dispute_creation_event_topic} )
        self.dispute_events = filter.get_all_entries()

    def event_date(self, event):
        return datetime.utcfromtimestamp(
            self.w3.eth.getBlock(event['blockNumber'])['timestamp']
        )

    def dispute(self, dispute_id):
        return KlerosDispute(dispute_id, kleros = self)

class KlerosDispute(Kleros):

    def __init__(self, dispute_id, kleros = None, node_url = None ):
        Kleros.__init__(self, node_url, kleros = kleros)
        self.dispute_id = dispute_id
        self.get_dispute_data()
        self.get_dispute_rounds()

    def get_dispute_data(self):
        raw_dispute = self.contract.functions.disputes(self.dispute_id).call()
        self.sub_court_id = int(raw_dispute[0])
        self.arbitrated = raw_dispute[1]
        self.number_of_choices = int(raw_dispute[2])
        self.period = int(raw_dispute[3])
        self.last_period_change = int(raw_dispute[4])
        self.draws_in_round = int(raw_dispute[5])
        self.commits_in_round = int(raw_dispute[6])
        self.ruled = bool(raw_dispute[7])

    def get_dispute_rounds(self):
        rounds_raw_data = self.contract.functions.getDispute(self.dispute_id).call()
        print(rounds_raw_data)
        self.rounds = []
        for i in range(0, len(rounds_raw_data[0])):
            round_data = [
                rounds_raw_data[0][i],rounds_raw_data[1][i],
                rounds_raw_data[2][i],rounds_raw_data[3][i],
                rounds_raw_data[4][i],rounds_raw_data[5][i]
            ]
            self.rounds.append(KlerosDisputeRound(self.dispute_id, i, round_data, kleros = self))
        self.last_round = self.rounds[-1]

    def get_creation_event(self):
        filter = self.contract.events.DisputeCreation.createFilter(fromBlock=self.initial_block,
            argument_filters={"topic0": self.dispute_creation_event_topic, "topic1": self.dispute_id} )
        self.creation_event = filter.get_all_entries()[0]
        self.address = self.creation_event['address']
        self.txid = self.creation_event['transactionHash']
        self.creation_date = self.event_date(self.creation_event)

    def current_ruling(self):
        self.ruling = self.contract.functions.currentRuling(self.dispute_id).call()
        return self.ruling

    # TODO Create methods: is_closed() is_open() and other statuses that return bool
    def dispute_status(self):
        self.current_status = self.contract.functions.disputeStatus(self.dispute_id).call()
        return self.current_status

    def winning_choice(self):
        if self.dispute_status() is None: return None
        return self.current_ruling()

class KlerosDisputeRound(Kleros):

    def __init__(self, dispute_id, round_id, round_data, kleros = None, node_url = None ):
        Kleros.__init__(self, node_url, kleros = kleros)

        self.dispute_id = dispute_id
        self.round_id = round_id
        self.votes_length = round_data[0]
        self.tokens_at_stake_per_juror = round_data[1] / 10 ** 18
        self.total_fees_for_jurors = round_data[2] / 10 ** 18
        self.votes_count = round_data[3]
        self.repartitions = round_data[4]
        self.penalties = round_data[5] / 10 ** 18

    def get_votes(self):
        self.votes = []
        for vote_id in range(self.votes_length):
            self.votes.append(KlerosVote(self.dispute_id, appeal, vote_id, contract = self.contract))
        return self.votes

    def get_vote_counter(self):
        data = self.contract.functions.getVoteCounter(self.dispute_id, self.round_id).call()
        return data[1]

    def get_PNK_at_stake(self):
        return self.tokens_at_stake_per_juror * self.votes_length

    def pending_votes(self):
        return self.votes_length - self.votes_count

    def losers(self):
        majority = self.votes_length // 2
        votes = self.get_vote_counter()
        self.losers = self.votes_length

        if votes[2] > majority:
            self.losers -= votes[2]
        elif votes[1] > majority:
            self.losers -= votes[1]
        elif votes[0] > majority:
            self.losers -= votes[0]
        else:
            self.losers = 0

        return self.losers

    def get_ETH_per_juror(self):
        return self.total_fees_for_jurors / self.votes_length


class KlerosVote(Kleros):
    def __init__(self, dispute_id, appeal, vote_id, kleros = None, node_url = None ):
        Kleros.__init__(self, node_url, kleros = kleros)
        self.data = self.get_vote(dispute_id, appeal, vote_id)

    def get_vote(self, case_number, appeal = 0, vote_id = 0):
        raw_vote = self.contract.functions.getVote(case_number, appeal, vote_id).call()
        self.account = raw_vote[0]
        self.commit = raw_vote[1]
        self.choice = int(raw_vote[2])
        self.vote = bool(raw_vote[3])
