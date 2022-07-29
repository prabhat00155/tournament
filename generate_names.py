import names
import sys

n = input('How many names you want to generate? ')
try:
    n = int(n)
except ValueError:
    print('Invalid input. Expected an integer.')
    sys.exit()
output = input('Enter the output filename(default: names.txt): ')
if not output:
    output = 'names.txt'
with open(output, 'w') as o_file:
    for i in range(n):
        name = names.get_full_name()
        o_file.write(f'{name}\n')
print(f'{output} created with {n} randomly generated names')
