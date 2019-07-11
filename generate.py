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
      for exist_game_idx in range(0, len(exist_round), 2):
         for comb_game_idx in range(0, len(combination), 2):
            if combination[comb_game_idx] == no_of_teams - 2:
               continue
            if exist_round[exist_game_idx] == combination[comb_game_idx] and \
               exist_round[exist_game_idx + 1] == combination[comb_game_idx + 1]:
                  return True
            if exist_round[exist_game_idx] == combination[comb_game_idx + 1] and \
                    exist_round[exist_game_idx] == combination[comb_game_idx + 1]:
               return True
   return False

def find_next_round(round_id, rounds):
   if round_id == no_of_rounds:
      return rounds
   combinations = list(itertools.permutations(range(no_of_teams - 2)))
   # combinations = list(itertools.permutations(range(no_of_teams)))
   for combination_tuple in combinations:
      combination = list(combination_tuple)
      combination.insert(round_id * 2, no_of_teams - 1)
      combination.insert(round_id * 2, no_of_teams - 2)
      # first round
      if len(rounds) == 0:
         print('ronde {}: {}'.format(round_id, rounds + [combination]))
         return find_next_round(round_id + 1, rounds + [combination])
      # other rounds
      if check_overlap(rounds, combination) or check_team_combination_already_exists(rounds, combination):
         continue
      print('ronde {}: {}'.format(round_id, rounds + [combination]))
      next = find_next_round(round_id + 1, rounds + [combination])
      if next:
         return next
      else:
         print('dead end...')
         continue

   return None

no_of_rounds = 6
# no_of_teams = no_of_rounds * 2 - 2
no_of_teams = no_of_rounds * 2

rounds = []

start = time.time()

rounds = find_next_round(0, rounds)


print('took {} seconds'.format(time.time() - start))

print('----------------------')
print('final solution')
print('----------------------')
if rounds:
    # heading
    print('                 spellen')
    print('         ', end='')
    for idx in range(no_of_rounds):
        print(' {}  '.format(idx + 1), end='')
    print('')
    print('--------', end='')
    for idx in range(no_of_rounds):
        print('----', end='')
    print('')

    # schedule
    for round_id, round in enumerate(rounds):
        print("ronde {}: ".format(round_id), end = '')
        for team in round:
            char = team if team < no_of_teams - 2 else '-'
            next_char = ' ' if team % 2 == 1 else '-'
            print('{}{}'.format(char, next_char), end='')
        print('')

else:
   print('no solution found')
