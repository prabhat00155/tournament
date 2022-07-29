import collections
import math
import random
import sys


groups = collections.defaultdict(list)

def random_pick(no_of_groups):
    while True:
        gid = random.randint(1, no_of_groups)
        if len(groups[gid]) < group_size:
            return gid

group_size = input('Enter group size(5 by default)')
if not group_size:
    group_size = 5
input_file = input('Enter input file name(names.txt by default)')
if not input_file:
    input_file = 'names.txt'
with open(input_file) as i_file:
    names = i_file.read()
players = names.strip().split('\n')
print(players)
no_of_groups = math.ceil(len(players) / group_size)
for player in players:
    gid = random_pick(no_of_groups)
    groups[gid].append(player)
for group in sorted(groups.keys()):
    print(f'Group {group}')
    print(groups[group])
