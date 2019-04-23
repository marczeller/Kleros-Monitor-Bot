#!/usr/bin/python3

import sys
from kleros import Kleros

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('monitor', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def call():
    node = 'https://mainnet.infura.io/v3/31c378f901bf46c08674e655e6640287'

    kleros = Kleros(node)
    case_Number = 17

    # Call kleros Smart-contract to get the total number of Jurors on current round

    dispute = kleros.dispute(case_Number)
    jurors_drawn = dispute['draws_in_round']

    # ("%s jurors drawn on last round" % jurors_drawn)
    j = jurors_drawn
    ###main function call
    return get_juror_votes(j, kleros, case_Number)

### Main function, needs optimazation
def get_juror_votes(j, kleros, case_Number):
  output = ''

  if j == 3 or j == 5:
    appeal = 0
  elif j == 7 or j == 11:
    appeal = 1
  elif j == 15 or j == 23:
    appeal = 2
  else:
    print("i haven't coded that part yet")
### loop that retrieves all jurors votes and puts them in a list
  jurorVotes = []
  for i in range(j):
    vote = kleros.get_vote(case_Number, appeal, i)
    jurorVotes.append(vote['choice'])

  ###user-oriented, give information of votes
  votesYes = jurorVotes.count(1)
  votesYes_ratio = (votesYes / j) * 100

  output += ("Yes votes: %s (%.2f %%)<br>" % (votesYes, votesYes_ratio))

  votesNo = jurorVotes.count(2)
  votesNo_ratio = (votesNo / j) * 100

  output += ("No votes:  %s (%.2f %%)<br>" % (votesNo, votesNo_ratio))

  HaventVotedyet = jurorVotes.count(0)
  if HaventVotedyet > 0:
    output += ("Pending votes: %s<br>" % HaventVotedyet)
  else:
    output += ("Eveyone voted.<br>")

  ###User-oriented, give information on majority reached or not
  if votesYes > j // 2 or votesNo > j // 2:
    output += ("Absolute majority was reached<br>")
  else:
    output += ("Case is still undecided<br>")

  ###simple way to define winner, probably will bug on some cases, need better logic
  jurorVotes.sort()

  index = (j // 2) + 1
  if jurorVotes[index] == 1:
      output += ("Outcome: Yes<br>")
  elif jurorVotes[index] == 2:
      output += ("Outcome: No<br>")
  else:
    output += ("Try again later to know if the case reached a majority.<br>")
  return output
