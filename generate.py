import itertools
import time


def check_overlap(rounds, combination):
    for exist_round in rounds:
       for colum_idx, column in enumerate(exist_round):
          if combination[colum_idx] == column:
             return True
          if colum_idx % 2 == 0 and combination[colum_idx + 1] == column:
             return True
          if colum_idx % 2 == 1 and combination[colum_idx - 1] == column:
             return True
    return False

def check_team_combination_already_exists(rounds, combination):
   for exist_round in rounds:
      for exist_game_idx in range(len(exist_round) / 2):
         for comb_game_idx in range(len(combination) / 2):
            if exist_round[exist_game_idx] == combination[comb_game_idx] and \
               exist_round[exist_game_idx + 1] == combination[comb_game_idx + 1]:
                  return True
   return False

no_of_rounds = 6
no_of_teams = no_of_rounds * 2

rounds = []

start = time.time()

for round_id, round in enumerate(range(no_of_rounds)):
   combinations = itertools.permutations(range(no_of_teams))
   for combination in combinations:
      # first round
      if len(rounds) == 0:
         rounds.append(combination)
         print('ronde {}: {}'.format(round_id, combination))
         break
      # other rounds
      if check_overlap(rounds, combination) or check_team_combination_already_exists(rounds, combination):
         continue
      rounds.append(combination)
      print('ronde {}: {}'.format(round_id, combination))
      break

print('took {} seconds'.format(time.time() - start))

print('----------------------')
print('final solution')
print('----------------------')
for round_id, round in enumerate(rounds):
   print('ronde {}: {}'.format(round_id, round))

