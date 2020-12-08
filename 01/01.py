import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  module_masses = [int(line.strip()) for line in file]


part_one = sum([x // 3 - 2 for x in module_masses])

calc_fuel = lambda x: 0 if x < 6 else x // 3 - 2 + calc_fuel(x // 3 - 2)
part_two = sum([calc_fuel(x) for x in module_masses])

print('Part One: %d' % part_one)
print('Part Two: %d' % part_two)
