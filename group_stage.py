import collections
import math
import random
import sys


def random_pick(no_of_groups, groups, group_size):
    while True:
        gid = random.randint(1, no_of_groups)
        if len(groups[gid]) < group_size:
            return gid


def assign_group(players, group_size):
    groups = collections.defaultdict(list)
    no_of_groups = math.ceil(len(players) / group_size)
    for player in players:
        gid = random_pick(no_of_groups, groups, group_size)
        groups[gid].append(player)
    return groups


def fetch_players(input_file):
    with open(input_file) as i_file:
        names = i_file.read()
    return names.strip().split('\n')


def display(groups, as_csv=False):
    if as_csv:
        for group in sorted(groups.keys()):
            print(f'Group {group}')
            players = ','.join(groups[group])
            print(f'Name,Wins,Losses,{players}')
            for player in groups[group]:
                print(player)
            print()
            print()
    else:
        for group in sorted(groups.keys()):
            print(f'Group {group}')
            print(groups[group])


def main():
    group_size = input('Enter group size(5 by default): ')
    try:
        group_size = 5 if not group_size else int(group_size)
    except ValueError:
        print('Invalid group size entered, expected an integer.')
        sys.exit()

    input_file = input('Enter input file name(names.txt by default): ')
    if not input_file:
        input_file = 'names.txt'

    players = fetch_players(input_file)
    groups = assign_group(players, group_size)
    display(groups, as_csv=True)


if __name__ == "__main__":
    main()
