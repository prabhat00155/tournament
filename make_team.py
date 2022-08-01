import collections
import random
import sys


def create_matches(players):
    matchup = []
    mapper = collections.defaultdict(bool)
    num = len(players)
    if num % 2 != 0:
        print('Please enter an even number of teams/players as input.')
        sys.exit()
    count = 0
    while count < num:
        flag = True
        while flag:
            team1 = random.randint(1, num)
            if not mapper[team1]:
                mapper[team1] = True
                flag = False
        flag = True
        while flag:
            team2 = random.randint(1, num)
            if not mapper[team2]:
                mapper[team2] = True
                flag = False
        count += 2
        matchup.append((players[team1 - 1], players[team2 - 1]))
    return matchup


def fetch_players(input_file):
    with open(input_file) as i_file:
        names = i_file.read()
    return names.strip().split('\n')


def main():
    input_file = input('Enter input file name(names.txt by default): ')
    if not input_file:
        input_file = 'names.txt'

    players = fetch_players(input_file)
    matchup = create_matches(players)
    for match in matchup:
        print(f'{match[0]} & {match[1]}')


if __name__ == "__main__":
    main()
