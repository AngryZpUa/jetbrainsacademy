import itertools
# the variable 'teams' is already defined

for play in itertools.combinations(teams, 2):
    print(play)
