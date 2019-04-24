#!/usr/bin/python3

import sys
from kleros import Kleros, KlerosDispute, KlerosVote

# TODO Move to ENV
node = 'https://mainnet.infura.io/v3/31c378f901bf46c08674e655e6640287'

case_Number = int(sys.argv[1])
dispute = KlerosDispute(case_Number, node=node)

### Call kleros Smart-contract to get the total number of Jurors on current round

print("%s jurors drawn on last round" % dispute.rounds[-1])

# TODO Move this to kleros.py as a function of KlerosDispute
def get_juror_votes():
    j = dispute.rounds[-1]

    jurorVotes = []
    for vote in dispute.get_votes():
        jurorVotes.append(vote.choice)

    ###user-oriented, give information of votes
    votesYes = jurorVotes.count(1)
    votesYes_ratio = (votesYes / j) * 100

    print("Yes votes: %s (%.2f %%)" % (votesYes, votesYes_ratio))

    votesNo = jurorVotes.count(2)
    votesNo_ratio = (votesNo / j) * 100

    print("No votes:    %s (%.2f %%)" % (votesNo, votesNo_ratio))

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

def at_stake(): # TODO Move this to kleros.py as a function of KlerosDispute
    case_closed = dispute.data['ruled']
    subcourt = dispute.data['sub_court_id']
    j = dispute.rounds[-1]

    if subcourt == 2:
            PNK_at_stake = j * 3750
            ETH_fee = j * 0.065
    elif subcourt == 3:
            PNK_at_stake = j * 40000
            ETH_fee = j * 0.55
    else:
        return ""
    if case_closed == True:
        print("The case is closed, a total of %s PNK was at stake and %s ETH was distributed to jurors" % (PNK_at_stake, ETH_fee))
    else:
        print("The case is still open, %s PNK are at stake and %s ETH will be distributed to jurors" % (PNK_at_stake, ETH_fee))

get_juror_votes()
at_stake()
