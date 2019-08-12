from web3 import Web3, HTTPProvider
from datetime import datetime

class KlerosEth:
    abi = '[{"constant":false,"inputs":[{"name":"_pinakion","type":"address"}],"name":"changePinakion","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"RNBlock","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"disputesWithoutJurors","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"passPhase","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"governor","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"lastDelayedSetStake","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_disputeID","type":"uint256"}],"name":"disputeStatus","outputs":[{"name":"status","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_disputeID","type":"uint256"}],"name":"passPeriod","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"maxDrawingTime","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_disputeID","type":"uint256"}],"name":"currentRuling","outputs":[{"name":"ruling","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"courts","outputs":[{"name":"parent","type":"uint96"},{"name":"hiddenVotes","type":"bool"},{"name":"minStake","type":"uint256"},{"name":"alpha","type":"uint256"},{"name":"feeForJuror","type":"uint256"},{"name":"jurorsForCourtJump","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_appeal","type":"uint256"},{"name":"_iterations","type":"uint256"}],"name":"execute","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"ALPHA_DIVISOR","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_voteIDs","type":"uint256[]"},{"name":"_choice","type":"uint256"},{"name":"_salt","type":"uint256"}],"name":"castVote","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_subcourtID","type":"uint96"},{"name":"_minStake","type":"uint256"}],"name":"changeSubcourtMinStake","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_subcourtID","type":"uint96"}],"name":"getSubcourt","outputs":[{"name":"children","type":"uint256[]"},{"name":"timesPerPeriod","type":"uint256[4]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"appeal","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"onTransfer","outputs":[{"name":"allowed","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"disputes","outputs":[{"name":"subcourtID","type":"uint96"},{"name":"arbitrated","type":"address"},{"name":"numberOfChoices","type":"uint256"},{"name":"period","type":"uint8"},{"name":"lastPeriodChange","type":"uint256"},{"name":"drawsInRound","type":"uint256"},{"name":"commitsInRound","type":"uint256"},{"name":"ruled","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_subcourtID","type":"uint96"},{"name":"_timesPerPeriod","type":"uint256[4]"}],"name":"changeSubcourtTimesPerPeriod","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_subcourtID","type":"uint96"},{"name":"_feeForJuror","type":"uint256"}],"name":"changeSubcourtJurorFee","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_subcourtID","type":"uint96"},{"name":"_alpha","type":"uint256"}],"name":"changeSubcourtAlpha","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_voteIDs","type":"uint256[]"},{"name":"_commit","type":"bytes32"}],"name":"castCommit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"RN","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"RNGenerator","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_destination","type":"address"},{"name":"_amount","type":"uint256"},{"name":"_data","type":"bytes"}],"name":"executeGovernorProposal","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_minStakingTime","type":"uint256"}],"name":"changeMinStakingTime","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"NON_PAYABLE_AMOUNT","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_subcourtID","type":"uint96"},{"name":"_stake","type":"uint128"}],"name":"setStake","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_disputeID","type":"uint256"}],"name":"executeRuling","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_appeal","type":"uint256"},{"name":"_voteID","type":"uint256"}],"name":"getVote","outputs":[{"name":"account","type":"address"},{"name":"commit","type":"bytes32"},{"name":"choice","type":"uint256"},{"name":"voted","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_RNGenerator","type":"address"}],"name":"changeRNGenerator","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_iterations","type":"uint256"}],"name":"executeDelayedSetStakes","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_account","type":"address"},{"name":"_subcourtID","type":"uint96"}],"name":"stakeOf","outputs":[{"name":"stake","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_subcourtID","type":"uint96"},{"name":"_jurorsForCourtJump","type":"uint256"}],"name":"changeSubcourtJurorsForJump","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_disputeID","type":"uint256"}],"name":"appealPeriod","outputs":[{"name":"start","type":"uint256"},{"name":"end","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"phase","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MAX_STAKE_PATHS","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"delayedSetStakes","outputs":[{"name":"account","type":"address"},{"name":"subcourtID","type":"uint96"},{"name":"stake","type":"uint128"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"lastPhaseChange","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"minStakingTime","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"nextDelayedSetStake","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_numberOfChoices","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"createDispute","outputs":[{"name":"disputeID","type":"uint256"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_iterations","type":"uint256"}],"name":"drawJurors","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_parent","type":"uint96"},{"name":"_hiddenVotes","type":"bool"},{"name":"_minStake","type":"uint256"},{"name":"_alpha","type":"uint256"},{"name":"_feeForJuror","type":"uint256"},{"name":"_jurorsForCourtJump","type":"uint256"},{"name":"_timesPerPeriod","type":"uint256[4]"},{"name":"_sortitionSumTreeK","type":"uint256"}],"name":"createSubcourt","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_account","type":"address"}],"name":"getJuror","outputs":[{"name":"subcourtIDs","type":"uint96[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"},{"name":"_amount","type":"uint256"}],"name":"onApprove","outputs":[{"name":"allowed","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"jurors","outputs":[{"name":"stakedTokens","type":"uint256"},{"name":"lockedTokens","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_maxDrawingTime","type":"uint256"}],"name":"changeMaxDrawingTime","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_disputeID","type":"uint256"}],"name":"getDispute","outputs":[{"name":"votesLengths","type":"uint256[]"},{"name":"tokensAtStakePerJuror","type":"uint256[]"},{"name":"totalFeesForJurors","type":"uint256[]"},{"name":"votesInEachRound","type":"uint256[]"},{"name":"repartitionsInEachRound","type":"uint256[]"},{"name":"penaltiesInEachRound","type":"uint256[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_appeal","type":"uint256"}],"name":"getVoteCounter","outputs":[{"name":"winningChoice","type":"uint256"},{"name":"counts","type":"uint256[]"},{"name":"tied","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_governor","type":"address"}],"name":"changeGovernor","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"MIN_JURORS","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"appealCost","outputs":[{"name":"cost","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_owner","type":"address"}],"name":"proxyPayment","outputs":[{"name":"allowed","type":"bool"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[],"name":"lockInsolventTransfers","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_extraData","type":"bytes"}],"name":"arbitrationCost","outputs":[{"name":"cost","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"pinakion","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"_governor","type":"address"},{"name":"_pinakion","type":"address"},{"name":"_RNGenerator","type":"address"},{"name":"_minStakingTime","type":"uint256"},{"name":"_maxDrawingTime","type":"uint256"},{"name":"_hiddenVotes","type":"bool"},{"name":"_minStake","type":"uint256"},{"name":"_alpha","type":"uint256"},{"name":"_feeForJuror","type":"uint256"},{"name":"_jurorsForCourtJump","type":"uint256"},{"name":"_timesPerPeriod","type":"uint256[4]"},{"name":"_sortitionSumTreeK","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_phase","type":"uint8"}],"name":"NewPhase","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_disputeID","type":"uint256"},{"indexed":false,"name":"_period","type":"uint8"}],"name":"NewPeriod","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_address","type":"address"},{"indexed":false,"name":"_subcourtID","type":"uint256"},{"indexed":false,"name":"_stake","type":"uint128"},{"indexed":false,"name":"_newTotalStake","type":"uint256"}],"name":"StakeSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_address","type":"address"},{"indexed":true,"name":"_disputeID","type":"uint256"},{"indexed":false,"name":"_appeal","type":"uint256"},{"indexed":false,"name":"_voteID","type":"uint256"}],"name":"Draw","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_address","type":"address"},{"indexed":true,"name":"_disputeID","type":"uint256"},{"indexed":false,"name":"_tokenAmount","type":"int256"},{"indexed":false,"name":"_ETHAmount","type":"int256"}],"name":"TokenAndETHShift","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_disputeID","type":"uint256"},{"indexed":true,"name":"_arbitrable","type":"address"}],"name":"DisputeCreation","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_disputeID","type":"uint256"},{"indexed":true,"name":"_arbitrable","type":"address"}],"name":"AppealPossible","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_disputeID","type":"uint256"},{"indexed":true,"name":"_arbitrable","type":"address"}],"name":"AppealDecision","type":"event"}]'

    kleros_address = '0x988b3A538b618C7A603e1c11Ab82Cd16dbE28069'
    initial_block = 7303699
    dispute_creation_event_topic = "0x141dfc18aa6a56fc816f44f0e9e2f1ebc92b15ab167770e17db5b084c10ed995"
    staking_event_topic = "0x8f753321c98641397daaca5e8abf8881fff1fd7a7bc229924a012e2cb61763d5"

    max_court_id = 4 # FIXME this should not be hardcoded, but I don't know where to get the info from yet

    def __init__(self, node_url):
        self.w3 = Web3(HTTPProvider(node_url, request_kwargs={'timeout': 60})) #FIXME Add Exceptions, errors
        self.contract = self.w3.eth.contract(
            address = Web3.toChecksumAddress(self.kleros_address),
            abi = self.abi
        )

    def dispute_events(self, starting_block = None):
        if starting_block == None: starting_block = self.initial_block
        try:
            filter = self.contract.events.DisputeCreation.createFilter(
                fromBlock=int(starting_block),
                # argument_filters={"topic0": self.dispute_creation_event_topic}
                topics = [self.dispute_creation_event_topic]
            )
            disputes = []
            for event in filter.get_all_entries():
                disputes.append({
                    'dispute_id' : event['args']['_disputeID'],
                    'date' : self.event_date(event),
                    'creator': self.event_creator(event),
                    'txid': event['transactionHash'].hex(),
                    'block_number': event['blockNumber']
                })
            return disputes
        except ValueError as e:
            return self.dispute_events(initial_block)

    def dispute_data(self, dispute_id):
        raw_dispute = self.contract.functions.disputes(dispute_id).call()
        ruling = self.contract.functions.currentRuling(dispute_id).call()
        current_status = self.contract.functions.disputeStatus(dispute_id).call()
        return {
            'subcourt_id': int(raw_dispute[0]),
            'arbitrated': raw_dispute[1],
            'number_of_choices': int(raw_dispute[2]),
            'period': int(raw_dispute[3]),
            'last_period_change': int(raw_dispute[4]),
            'draws_in_round': int(raw_dispute[5]),
            'commits_in_round': int(raw_dispute[6]),
            'ruled': bool(raw_dispute[7]),
            'ruling': ruling,
            'current_status': current_status
        }

    def event_date(self, event):
        return datetime.utcfromtimestamp(
            self.w3.eth.getBlock(event['blockNumber'])['timestamp']
        )

    def event_creator(self, event):
        txid = event['transactionHash']
        tx = self.w3.eth.getTransaction(txid)
        return tx['from']

    def dispute_rounds(self, dispute_id):
        rounds_raw_data = self.contract.functions.getDispute(dispute_id).call()
        rounds = []
        for i in range(0, len(rounds_raw_data[0])):
            rounds.append({
                'jury_size': rounds_raw_data[0][i],
                'tokens_at_stake_per_juror': rounds_raw_data[1][i] / 10**18,
                'total_fees': rounds_raw_data[2][i]/ 10**18,
                'votes': rounds_raw_data[3][i],
                'repartition': rounds_raw_data[4][i],
                'penalties': rounds_raw_data[5][i] / 10**18
            })
        return(rounds)

    def vote_counts(self, dispute_id, round):
        data = self.contract.functions.getVoteCounter(dispute_id, round).call()
        return {
            'winning_choice': data[0],
            'counts': data[1],
            'tied': data[2]
        }

    def vote(self, dispute_id, round, vote_id):
        raw_vote = self.contract.functions.getVote(dispute_id, round, vote_id).call()
        return {
            'address': raw_vote[0],
            'commit': raw_vote[1].hex(),
            'choice': int(raw_vote[2]),
            'vote': bool(raw_vote[3])
        }

    def staking_events(self, starting_block = None):
        if starting_block == None: starting_block = self.initial_block
        try:
            filter = self.contract.events.StakeSet.createFilter(
                fromBlock=int(starting_block),
                topics = [ self.staking_event_topic ]
            )
            stakings = []
            for staking in filter.get_all_entries():
                stakings.append({
                    'address': staking['args']['_address'],
                    'staked': staking['args']['_newTotalStake'] / 10**18,
                    'court_id': staking['args']['_subcourtID'],
                    'txid': staking['transactionHash'].hex(),
                    'date' : self.event_date(staking),
                    'block_number': staking['blockNumber']
                })
            return stakings
        except ValueError as e:
            return self.staking_events(initial_block)
