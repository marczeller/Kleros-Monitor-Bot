#!/usr/bin/python3

import sys
from kleros import Kleros

node = 'https://mainnet.infura.io/v3/31c378f901bf46c08674e655e6640287'

kleros = Kleros(node)

case_Number = int(sys.argv[1])

### Call kleros Smart-contract to get the total number of Jurors on current round

dispute = kleros.dispute(case_Number)
jurors_drawn = dispute['draws_in_round']

print("%s jurors drawn on last round" % jurors_drawn)
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
    vote = kleros.get_vote(case_Number, appeal, i)
    jurorVotes.append(vote['choice'])

  ###user-oriented, give information of votes
  votesYes = jurorVotes.count(1)
  votesYes_ratio = (votesYes / j) * 100

  print("Yes votes: %s (%.2f %%)" % (votesYes, votesYes_ratio))

  votesNo = jurorVotes.count(2)
  votesNo_ratio = (votesNo / j) * 100

  print("No votes:  %s (%.2f %%)" % (votesNo, votesNo_ratio))

  HaventVotedyet = jurorVotes.count(0)
  if HaventVotedyet > 0:
    print("Pending votes: %s" % HaventVotedyet)
  else:
    print("Eveyone voted.")

  ###User-oriented, give information on majority reached or not
  if votesYes > j // 2 or votesNo > j // 2:
    print("Absolute majority was reached")
  else:
    print("Case is still undecided")

  ###simple way to define winner, probably will bug on some cases, need better logic
  jurorVotes.sort()

  index = (j // 2) + 1
  if jurorVotes[index] == 1:
      print("Outcome: Yes")
  elif jurorVotes[index] == 2:
      print("Outcome: No")
  else:
    print("Try again later to know if the case reached a majority.")
  case_closed = dispute['ruled']
  if case_closed == True:
      print("The case is closed PNK and ETH was distributed to jurors")
  else:
      print("This case is still open, Stay tuned")

###main function call
get_juror_votes(j)
