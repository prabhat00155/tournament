# tournament

This enables users to generate their own tournament groups given a list of players, number of groups, number of persons per group.

To create a file with random participant names run:
```
python generate_names.py 
```
To group the participants, run:
```
python group_stage.py
```
To create a knockout stage of a tournament(given the number of paricipants), run:
```
python knockout.py
```
To create a seeded knockout stage where group winners play runner's up from other groups(given the number of groups):
```
python seeded_knockout.py
```

