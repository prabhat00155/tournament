import collections
import random
import sys


def create_matches(num):
    matchup = []
    winners = collections.defaultdict(bool)
    runners_up = collections.defaultdict(bool)
    if num % 2 != 0:
        print('Please enter an even number of teams/players as input.')
        sys.exit()
    count = 0
    while count < num:
        flag = True
        while flag:
            team1 = random.randint(1, num)
            if not winners[team1]:
                winners[team1] = True
                flag = False
        flag = True
        while flag:
            team2 = random.randint(1, num)
            if not runners_up[team2] and team1 != team2:
                runners_up[team2] = True
                flag = False
        count += 1
        matchup.append((team1, team2))
    return matchup

def main():
    num = input("Enter the number of groups(default = 32): ")
    try:
        num = int(num) if num else 32
    except ValueError:
        print('Invalid number of players/teams entered, expected an integer.')
        sys.exit()
    matchup = create_matches(num)
    for match in matchup:
        print(f'Group {match[0]} winner\nvs\nGroup {match[1]} runner-up')


if __name__ == "__main__":
    main()
