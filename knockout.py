import collections
import random
import sys


def create_matches(num):
    matchup = []
    mapper = collections.defaultdict(bool)
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
        matchup.append((team1, team2))
    return matchup

def main():
    num = input("Enter the number of players/teams(default = 32): ")
    try:
        num = int(num) if num else 32
    except ValueError:
        print('Invalid number of players/teams entered, expected an integer.')
        sys.exit()
    matchup = create_matches(num)
    for match in matchup:
        print(f'Player {match[0]} vs Player {match[1]}')


if __name__ == "__main__":
    main()
