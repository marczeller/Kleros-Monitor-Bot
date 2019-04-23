#!/usr/bin/python3

import sys
from kleros import Kleros

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('monitor', __name__, url_prefix='/')

@bp.route('/dispute/<dispute_id>', methods=['GET'])
def call(dispute_id):
    node = 'https://mainnet.infura.io/v3/31c378f901bf46c08674e655e6640287'

    kleros = Kleros(node)
    case_Number = int(dispute_id)

    # Call kleros Smart-contract to get the total number of Jurors on current round

    dispute = kleros.dispute(case_Number)
    jurors_drawn = dispute['draws_in_round']

    # ("%s jurors drawn on last round" % jurors_drawn)
    j = jurors_drawn
    ###main function call
    output = get_juror_votes(j, kleros, case_Number)
    return render_template('monitor/disputes.html', output=output)
### Main function, needs optimazation
def get_juror_votes(j, kleros, case_Number):
  output = {'dispute_id': case_Number, 'juror_count': j}

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

  output['yes'] = "%s (%.2f %%)" % (votesYes, votesYes_ratio)

  votesNo = jurorVotes.count(2)
  votesNo_ratio = (votesNo / j) * 100

  output['no'] = "%s (%.2f %%)" % (votesNo, votesNo_ratio)

  HaventVotedyet = jurorVotes.count(0)
  output['pending'] = HaventVotedyet

  ###User-oriented, give information on majority reached or not
  if votesYes > j // 2 or votesNo > j // 2:
    output['majority'] = ("Yes")
  else:
    output['majority'] = ("No")

  ###simple way to define winner, probably will bug on some cases, need better logic
  jurorVotes.sort()

  index = (j // 2) + 1
  if jurorVotes[index] == 1:
      output['outcome'] = ("Yes")
  elif jurorVotes[index] == 2:
      output['outcome'] = ("No")
  else:
    output['outcome'] = ("Undecided")
  return output
