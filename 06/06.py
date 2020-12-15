import os

orbits = {}

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  for line in file:
    parent, child = line.strip().split(')')
    orbits[child] = parent

def find_parents(child):
  parents = set()
  while child in orbits:
    parents.add(orbits[child])
    child = orbits[child]
  return parents

print('Part One: %d' % sum([len(find_parents(x)) for x in orbits]))
print('Part Two: %d' % len(find_parents('YOU') ^ find_parents('SAN')))
