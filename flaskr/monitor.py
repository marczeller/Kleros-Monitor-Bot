#!/usr/bin/python3

from kleros import Kleros, KlerosDispute

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('monitor', __name__, url_prefix='/')

@bp.route('/dispute/<dispute_id>', methods=['GET'])
def dispute(dispute_id):

    node = 'https://mainnet.infura.io/v3/31c378f901bf46c08674e655e6640287'

    # Call kleros Smart-contract to get the total number of Jurors on current round
    dispute = KlerosDispute(node, int(dispute_id))
    j = dispute.data['draws_in_round']

    ###main function call
    output = get_juror_votes(j, dispute, int(dispute_id))
    return render_template('monitor/dispute.html', output=output)

### Main function, needs optimazation
def get_juror_votes(j, kleros, case_Number):
  output = {
    'dispute_id': case_Number,
    'juror_count': j
  }

  appeal = 0
  if j == 7  or j == 11: appeal = 1
  if j == 15 or j == 23: appeal = 2

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
    output['decided'] = "Yes"
  else:
    output['decided'] = "No"

  ###simple way to define winner, probably will bug on some cases, need better logic
  jurorVotes.sort()

  index = (j // 2) + 1
  if jurorVotes[index] == 1:
      output['final'] = "Yes"
  elif jurorVotes[index] == 2:
      output['final'] = "No"
  else:
    output['final'] = "Undecided"
  return output
