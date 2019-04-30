from web3 import Web3, HTTPProvider

class Kleros:
    abi = '[{"constant":false,"inputs":[{"name":"_pinakion","type":"address"}],"name":"changePinakion","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"RNBlock","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"disputesWithoutJurors","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"passPhase","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"governor","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"lastDelayedSetStake","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_disputeID","type":"uint256"}],"name":"disputeStatus","outputs":[{"name":"status","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_disputeID","type":"uint256"}],"name":"passPeriod","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"maxDrawingTime","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_disputeID","type":"uint256"}],"name":"currentRuling","outputs":[{"name":"ruling","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"courts","outputs":[{"name":"parent","type":"uint96"},{"name":"hiddenVotes","type":"bool"},{"name":"minStake","type":"uint256"},{"name":"alpha","type":"uint256"},{"name":"feeForJuror","type":"uint256"},{"name":"jurorsForCourtJump","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_appeal","type":"uint256"},{"name":"_iterations","type":"uint256"}],"name":"execute","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"ALPHA_DIVISOR","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_voteIDs","type":"uint256[]"},{"name":"_choice","type":"uint256"},{"name":"_salt","type":"uint256"}],"name":"castVote","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_subcourtID","type":"uint96"},{"name":"_minStake","type":"uint256"}],"name":"changeSubcourtMinStake","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_subcourtID","type":"uint96"}],"name":"getSubcourt","outputs":[{"name":"children","type":"uint256[]"},{"name":"timesPerPeriod","type":"uint256[4]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"appeal","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"onTransfer","outputs":[{"name":"allowed","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"disputes","outputs":[{"name":"subcourtID","type":"uint96"},{"name":"arbitrated","type":"address"},{"name":"numberOfChoices","type":"uint256"},{"name":"period","type":"uint8"},{"name":"lastPeriodChange","type":"uint256"},{"name":"drawsInRound","type":"uint256"},{"name":"commitsInRound","type":"uint256"},{"name":"ruled","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_subcourtID","type":"uint96"},{"name":"_timesPerPeriod","type":"uint256[4]"}],"name":"changeSubcourtTimesPerPeriod","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_subcourtID","type":"uint96"},{"name":"_feeForJuror","type":"uint256"}],"name":"changeSubcourtJurorFee","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_subcourtID","type":"uint96"},{"name":"_alpha","type":"uint256"}],"name":"changeSubcourtAlpha","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_voteIDs","type":"uint256[]"},{"name":"_commit","type":"bytes32"}],"name":"castCommit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"RN","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"RNGenerator","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_destination","type":"address"},{"name":"_amount","type":"uint256"},{"name":"_data","type":"bytes"}],"name":"executeGovernorProposal","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_minStakingTime","type":"uint256"}],"name":"changeMinStakingTime","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"NON_PAYABLE_AMOUNT","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_subcourtID","type":"uint96"},{"name":"_stake","type":"uint128"}],"name":"setStake","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_disputeID","type":"uint256"}],"name":"executeRuling","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_appeal","type":"uint256"},{"name":"_voteID","type":"uint256"}],"name":"getVote","outputs":[{"name":"account","type":"address"},{"name":"commit","type":"bytes32"},{"name":"choice","type":"uint256"},{"name":"voted","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_RNGenerator","type":"address"}],"name":"changeRNGenerator","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_iterations","type":"uint256"}],"name":"executeDelayedSetStakes","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_account","type":"address"},{"name":"_subcourtID","type":"uint96"}],"name":"stakeOf","outputs":[{"name":"stake","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_subcourtID","type":"uint96"},{"name":"_jurorsForCourtJump","type":"uint256"}],"name":"changeSubcourtJurorsForJump","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_disputeID","type":"uint256"}],"name":"appealPeriod","outputs":[{"name":"start","type":"uint256"},{"name":"end","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"phase","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MAX_STAKE_PATHS","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"delayedSetStakes","outputs":[{"name":"account","type":"address"},{"name":"subcourtID","type":"uint96"},{"name":"stake","type":"uint128"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"lastPhaseChange","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"minStakingTime","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"nextDelayedSetStake","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_numberOfChoices","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"createDispute","outputs":[{"name":"disputeID","type":"uint256"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_iterations","type":"uint256"}],"name":"drawJurors","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_parent","type":"uint96"},{"name":"_hiddenVotes","type":"bool"},{"name":"_minStake","type":"uint256"},{"name":"_alpha","type":"uint256"},{"name":"_feeForJuror","type":"uint256"},{"name":"_jurorsForCourtJump","type":"uint256"},{"name":"_timesPerPeriod","type":"uint256[4]"},{"name":"_sortitionSumTreeK","type":"uint256"}],"name":"createSubcourt","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_account","type":"address"}],"name":"getJuror","outputs":[{"name":"subcourtIDs","type":"uint96[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"},{"name":"_amount","type":"uint256"}],"name":"onApprove","outputs":[{"name":"allowed","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"jurors","outputs":[{"name":"stakedTokens","type":"uint256"},{"name":"lockedTokens","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_maxDrawingTime","type":"uint256"}],"name":"changeMaxDrawingTime","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_disputeID","type":"uint256"}],"name":"getDispute","outputs":[{"name":"votesLengths","type":"uint256[]"},{"name":"tokensAtStakePerJuror","type":"uint256[]"},{"name":"totalFeesForJurors","type":"uint256[]"},{"name":"votesInEachRound","type":"uint256[]"},{"name":"repartitionsInEachRound","type":"uint256[]"},{"name":"penaltiesInEachRound","type":"uint256[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_appeal","type":"uint256"}],"name":"getVoteCounter","outputs":[{"name":"winningChoice","type":"uint256"},{"name":"counts","type":"uint256[]"},{"name":"tied","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_governor","type":"address"}],"name":"changeGovernor","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"MIN_JURORS","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"appealCost","outputs":[{"name":"cost","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_owner","type":"address"}],"name":"proxyPayment","outputs":[{"name":"allowed","type":"bool"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[],"name":"lockInsolventTransfers","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_extraData","type":"bytes"}],"name":"arbitrationCost","outputs":[{"name":"cost","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"pinakion","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"_governor","type":"address"},{"name":"_pinakion","type":"address"},{"name":"_RNGenerator","type":"address"},{"name":"_minStakingTime","type":"uint256"},{"name":"_maxDrawingTime","type":"uint256"},{"name":"_hiddenVotes","type":"bool"},{"name":"_minStake","type":"uint256"},{"name":"_alpha","type":"uint256"},{"name":"_feeForJuror","type":"uint256"},{"name":"_jurorsForCourtJump","type":"uint256"},{"name":"_timesPerPeriod","type":"uint256[4]"},{"name":"_sortitionSumTreeK","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_phase","type":"uint8"}],"name":"NewPhase","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_disputeID","type":"uint256"},{"indexed":false,"name":"_period","type":"uint8"}],"name":"NewPeriod","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_address","type":"address"},{"indexed":false,"name":"_subcourtID","type":"uint256"},{"indexed":false,"name":"_stake","type":"uint128"},{"indexed":false,"name":"_newTotalStake","type":"uint256"}],"name":"StakeSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_address","type":"address"},{"indexed":true,"name":"_disputeID","type":"uint256"},{"indexed":false,"name":"_appeal","type":"uint256"},{"indexed":false,"name":"_voteID","type":"uint256"}],"name":"Draw","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_address","type":"address"},{"indexed":true,"name":"_disputeID","type":"uint256"},{"indexed":false,"name":"_tokenAmount","type":"int256"},{"indexed":false,"name":"_ETHAmount","type":"int256"}],"name":"TokenAndETHShift","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_disputeID","type":"uint256"},{"indexed":true,"name":"_arbitrable","type":"address"}],"name":"DisputeCreation","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_disputeID","type":"uint256"},{"indexed":true,"name":"_arbitrable","type":"address"}],"name":"AppealPossible","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_disputeID","type":"uint256"},{"indexed":true,"name":"_arbitrable","type":"address"}],"name":"AppealDecision","type":"event"}]'

    kleros_address = '0x988b3A538b618C7A603e1c11Ab82Cd16dbE28069'

    def __init__(self, node_url):
        w3 = Web3(HTTPProvider(node_url)) #TODO Exceptions, errors
        self.connection = w3.eth.contract(
            address = Web3.toChecksumAddress(self.kleros_address),
            abi = self.abi
        )

class KlerosDispute(Kleros):

    def __init__(self, dispute_id, kleros = None, node_url = None ):
        if kleros == None: Kleros.__init__(self, node_url)
        else: self.connection = kleros.connection
        self.dispute_id = dispute_id
        self.get_dispute()
        self.get_dispute_meta()

    # votesLengths uint256[], tokensAtStakePerJuror uint256[], totalFeesForJurors uint256[], votesInEachRound uint256[], repartitionsInEachRound uint256[], penaltiesInEachRound uint256[]
    def get_dispute_meta(self):
        data = self.connection.functions.getDispute(self.dispute_id).call()
        self.rounds = data[0]
        self.pnk_staked = data[1]
        self.eth_staked = data[2]

    def get_vote_counter(self, appeal = None):
        if appeal == None: appeal = len(self.rounds) - 1
        data = self.connection.functions.getVoteCounter(self.dispute_id, appeal).call()
        return data[1]

    def get_dispute(self):
        raw_dispute = self.connection.functions.disputes(self.dispute_id).call()
        self.sub_court_id = int(raw_dispute[0])
        self.arbitrated = raw_dispute[1]
        self.number_of_choices = int(raw_dispute[2])
        self.period = int(raw_dispute[3])
        self.last_period_change = int(raw_dispute[4])
        self.draws_in_round = int(raw_dispute[5])
        self.commits_in_round = int(raw_dispute[6])
        self.ruled = bool(raw_dispute[7])

    def get_votes(self, appeal = None):
        if appeal == None: appeal = len(self.rounds) - 1
        self.votes = []
        for vote_id in range(self.draws_in_round):
            self.votes.append(KlerosVote(self.dispute_id, appeal, vote_id, connection = self.connection))
        return self.votes

    def get_PNK_at_stake(self, appeal = None):
        if appeal == None: appeal = len(self.rounds) - 1
        return (self.pnk_staked[appeal] * self.draws_in_round) / 10 ** 18

    def get_ETH_at_stake(self, appeal = None):
        if appeal == None: appeal = len(self.rounds) - 1
        return self.eth_staked[appeal] / 10 ** 18

    def current_ruling(self):
        self.ruling = self.connection.functions.currentRuling(self.dispute_id).call()
        return self.ruling

    def dispute_status(self):
        self.current_status = self.connection.functions.disputeStatus(self.dispute_id).call()
        return self.current_status

    def pending_vote(self):
        self.pending_votes = self.draws_in_round - (self.get_vote_counter()[0] + self.get_vote_counter()[1] + self.get_vote_counter()[2])
        return self.pending_votes

    def define_losers(self):
        if self.get_vote_counter()[2] > self.draws_in_round // 2:
          self.losers = (self.get_vote_counter()[1] + self.get_vote_counter()[0] + self.pending_vote())
        elif self.get_vote_counter()[1] > self.draws_in_round // 2:
          self.losers = (self.get_vote_counter()[2] + self.get_vote_counter()[0] + self.pending_vote())
        elif self.get_vote_counter()[0] > self.draws_in_round // 2:
          self.losers = (self.get_vote_counter()[1] + self.get_vote_counter()[2] + self.pending_vote())
        else:
            self.losers = 0
        return self.losers

    def winning_choice(self):
        if self.dispute_status() is None: return None
        return self.current_ruling()

class KlerosVote(Kleros):
    def __init__(self, dispute_id, appeal, vote_id, kleros = None, node_url = None ):
        if kleros == None: Kleros.__init__(self, node_url)
        else: self.connection = kleros.connection
        self.data = self.get_vote(dispute_id, appeal, vote_id)

    def get_vote(self, case_number, appeal = 0, vote_id = 0):
        raw_vote = self.connection.functions.getVote(case_number, appeal, vote_id).call()
        self.account = raw_vote[0]
        self.commit = raw_vote[1]
        self.choice = int(raw_vote[2])
        self.vote = bool(raw_vote[3])
