#!/usr/bin/python3

from time import sleep
from web3 import Web3,HTTPProvider

### this is my public infura API, feel free to use yours
w3 = Web3(HTTPProvider('https://mainnet.infura.io/v3/31c378f901bf46c08674e655e6640287',request_kwargs={'timeout':60}))

### plug the script to the Kleros Smart-Contract

abi = '[{"constant":false,"inputs":[{"name":"_pinakion","type":"address"}],"name":"changePinakion","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"RNBlock","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"disputesWithoutJurors","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"passPhase","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"governor","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"lastDelayedSetStake","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_disputeID","type":"uint256"}],"name":"disputeStatus","outputs":[{"name":"status","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_disputeID","type":"uint256"}],"name":"passPeriod","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"maxDrawingTime","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_disputeID","type":"uint256"}],"name":"currentRuling","outputs":[{"name":"ruling","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"courts","outputs":[{"name":"parent","type":"uint96"},{"name":"hiddenVotes","type":"bool"},{"name":"minStake","type":"uint256"},{"name":"alpha","type":"uint256"},{"name":"feeForJuror","type":"uint256"},{"name":"jurorsForCourtJump","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_appeal","type":"uint256"},{"name":"_iterations","type":"uint256"}],"name":"execute","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"ALPHA_DIVISOR","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_voteIDs","type":"uint256[]"},{"name":"_choice","type":"uint256"},{"name":"_salt","type":"uint256"}],"name":"castVote","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_subcourtID","type":"uint96"},{"name":"_minStake","type":"uint256"}],"name":"changeSubcourtMinStake","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_subcourtID","type":"uint96"}],"name":"getSubcourt","outputs":[{"name":"children","type":"uint256[]"},{"name":"timesPerPeriod","type":"uint256[4]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"appeal","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"onTransfer","outputs":[{"name":"allowed","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"disputes","outputs":[{"name":"subcourtID","type":"uint96"},{"name":"arbitrated","type":"address"},{"name":"numberOfChoices","type":"uint256"},{"name":"period","type":"uint8"},{"name":"lastPeriodChange","type":"uint256"},{"name":"drawsInRound","type":"uint256"},{"name":"commitsInRound","type":"uint256"},{"name":"ruled","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_subcourtID","type":"uint96"},{"name":"_timesPerPeriod","type":"uint256[4]"}],"name":"changeSubcourtTimesPerPeriod","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_subcourtID","type":"uint96"},{"name":"_feeForJuror","type":"uint256"}],"name":"changeSubcourtJurorFee","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_subcourtID","type":"uint96"},{"name":"_alpha","type":"uint256"}],"name":"changeSubcourtAlpha","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_voteIDs","type":"uint256[]"},{"name":"_commit","type":"bytes32"}],"name":"castCommit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"RN","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"RNGenerator","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_destination","type":"address"},{"name":"_amount","type":"uint256"},{"name":"_data","type":"bytes"}],"name":"executeGovernorProposal","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_minStakingTime","type":"uint256"}],"name":"changeMinStakingTime","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"NON_PAYABLE_AMOUNT","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_subcourtID","type":"uint96"},{"name":"_stake","type":"uint128"}],"name":"setStake","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_disputeID","type":"uint256"}],"name":"executeRuling","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_appeal","type":"uint256"},{"name":"_voteID","type":"uint256"}],"name":"getVote","outputs":[{"name":"account","type":"address"},{"name":"commit","type":"bytes32"},{"name":"choice","type":"uint256"},{"name":"voted","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_RNGenerator","type":"address"}],"name":"changeRNGenerator","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_iterations","type":"uint256"}],"name":"executeDelayedSetStakes","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_account","type":"address"},{"name":"_subcourtID","type":"uint96"}],"name":"stakeOf","outputs":[{"name":"stake","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_subcourtID","type":"uint96"},{"name":"_jurorsForCourtJump","type":"uint256"}],"name":"changeSubcourtJurorsForJump","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_disputeID","type":"uint256"}],"name":"appealPeriod","outputs":[{"name":"start","type":"uint256"},{"name":"end","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"phase","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MAX_STAKE_PATHS","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"delayedSetStakes","outputs":[{"name":"account","type":"address"},{"name":"subcourtID","type":"uint96"},{"name":"stake","type":"uint128"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"lastPhaseChange","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"minStakingTime","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"nextDelayedSetStake","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_numberOfChoices","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"createDispute","outputs":[{"name":"disputeID","type":"uint256"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_iterations","type":"uint256"}],"name":"drawJurors","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_parent","type":"uint96"},{"name":"_hiddenVotes","type":"bool"},{"name":"_minStake","type":"uint256"},{"name":"_alpha","type":"uint256"},{"name":"_feeForJuror","type":"uint256"},{"name":"_jurorsForCourtJump","type":"uint256"},{"name":"_timesPerPeriod","type":"uint256[4]"},{"name":"_sortitionSumTreeK","type":"uint256"}],"name":"createSubcourt","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_account","type":"address"}],"name":"getJuror","outputs":[{"name":"subcourtIDs","type":"uint96[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"},{"name":"_amount","type":"uint256"}],"name":"onApprove","outputs":[{"name":"allowed","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"jurors","outputs":[{"name":"stakedTokens","type":"uint256"},{"name":"lockedTokens","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_maxDrawingTime","type":"uint256"}],"name":"changeMaxDrawingTime","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_disputeID","type":"uint256"}],"name":"getDispute","outputs":[{"name":"votesLengths","type":"uint256[]"},{"name":"tokensAtStakePerJuror","type":"uint256[]"},{"name":"totalFeesForJurors","type":"uint256[]"},{"name":"votesInEachRound","type":"uint256[]"},{"name":"repartitionsInEachRound","type":"uint256[]"},{"name":"penaltiesInEachRound","type":"uint256[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_appeal","type":"uint256"}],"name":"getVoteCounter","outputs":[{"name":"winningChoice","type":"uint256"},{"name":"counts","type":"uint256[]"},{"name":"tied","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_governor","type":"address"}],"name":"changeGovernor","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"MIN_JURORS","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_disputeID","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"appealCost","outputs":[{"name":"cost","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_owner","type":"address"}],"name":"proxyPayment","outputs":[{"name":"allowed","type":"bool"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[],"name":"lockInsolventTransfers","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_extraData","type":"bytes"}],"name":"arbitrationCost","outputs":[{"name":"cost","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"pinakion","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"_governor","type":"address"},{"name":"_pinakion","type":"address"},{"name":"_RNGenerator","type":"address"},{"name":"_minStakingTime","type":"uint256"},{"name":"_maxDrawingTime","type":"uint256"},{"name":"_hiddenVotes","type":"bool"},{"name":"_minStake","type":"uint256"},{"name":"_alpha","type":"uint256"},{"name":"_feeForJuror","type":"uint256"},{"name":"_jurorsForCourtJump","type":"uint256"},{"name":"_timesPerPeriod","type":"uint256[4]"},{"name":"_sortitionSumTreeK","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_phase","type":"uint8"}],"name":"NewPhase","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_disputeID","type":"uint256"},{"indexed":false,"name":"_period","type":"uint8"}],"name":"NewPeriod","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_address","type":"address"},{"indexed":false,"name":"_subcourtID","type":"uint256"},{"indexed":false,"name":"_stake","type":"uint128"},{"indexed":false,"name":"_newTotalStake","type":"uint256"}],"name":"StakeSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_address","type":"address"},{"indexed":true,"name":"_disputeID","type":"uint256"},{"indexed":false,"name":"_appeal","type":"uint256"},{"indexed":false,"name":"_voteID","type":"uint256"}],"name":"Draw","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_address","type":"address"},{"indexed":true,"name":"_disputeID","type":"uint256"},{"indexed":false,"name":"_tokenAmount","type":"int256"},{"indexed":false,"name":"_ETHAmount","type":"int256"}],"name":"TokenAndETHShift","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_disputeID","type":"uint256"},{"indexed":true,"name":"_arbitrable","type":"address"}],"name":"DisputeCreation","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_disputeID","type":"uint256"},{"indexed":true,"name":"_arbitrable","type":"address"}],"name":"AppealPossible","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_disputeID","type":"uint256"},{"indexed":true,"name":"_arbitrable","type":"address"}],"name":"AppealDecision","type":"event"}]'
klerosLiquid_address = '0x988b3A538b618C7A603e1c11Ab82Cd16dbE28069'


klerosLiquid_address = Web3.toChecksumAddress(klerosLiquid_address)

kleros_contract =  w3.eth.contract(
address = klerosLiquid_address,
abi = abi
)

### Ask the user for his case number, only input needed from user.

case_Number = input("what is your case number ? ")
case_Number = int(case_Number)

###probably useless, might remove that part later
print()
print("checking statuts of case " + str(case_Number))
print("...")
sleep(2)

### Call kleros Smart-contract to get the total number of Jurors on current round

jurors_drawn = kleros_contract.functions.disputes(case_Number).call()
jurors_drawn = int(jurors_drawn[5])
print("this case had " + str(jurors_drawn) + " jurors")
print("...")
j = jurors_drawn

### Main function, needs optimazation
def get_juror_votes(j):
### this is stupid as fuck, needs better logic, T²CR cases starts with n = 3 and Badge request starts with n = 5 then n*2+1 at each appeal
  if j == 3 or j == 5:
    appeal = 0
  elif j == 7 or j == 11:
    appeal = 1
  elif j == 15 or j == 23:
    appeal = 2  
  else:
    print("i haven't coded that part yet")
### loop that retrieve all jurors votes and put it in a list  
  jurorVotes = []
  for i in range(j):
    vote = kleros_contract.functions.getVote(case_Number,appeal,i).call()
    vote = vote[2]
    jurorVotes.append(vote)
  
  print()
  ###user-oriented, give information of votes
  votesYes = jurorVotes.count(1)
  print("the amount of yes votes is : ", votesYes)

  print()
  
  VotesNo = jurorVotes.count(2)
  print("the amount of No votes is : ", VotesNo)
  print()
  
  HaventVotedyet = jurorVotes.count(0)
  print("the remaining pending votes number is : ", HaventVotedyet)
  print()
  
  ###User-oriented, give information on majority reached or not
  if votesYes > j // 2 or VotesNo > j // 2:
    print("This case have reached an absolute majority !")
  else:
    print("The fate of this case is still undecided")  

  print()
  
  ###simple way to define winner, probably will bug on some cases, need better logic
  jurorVotes.sort()
  
  index = (j // 2) + 1
  if jurorVotes[index] == 1:
    print("Winning choice is Yes")
  elif jurorVotes[index] == 2:
    print("Winning choice is No")
  else:
    print("try again later to know if the case reached a majority !")

###main function call
get_juror_votes(j)

