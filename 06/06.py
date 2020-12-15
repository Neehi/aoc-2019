import os

orbits = {}

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  for line in file:
    parent, child = line.strip().split(')')
    orbits[child] = parent

def count_orbits(child):
  return 0 if child not in orbits else 1 + count_orbits(orbits[child])

def find_parents(child):
  parents = []
  while child in orbits:
    parents.append(orbits[child])
    child = orbits[child]
  return parents

print('Part One: %d' % sum([count_orbits(x) for x in orbits]))

you_parents = find_parents('YOU')
santa_parents = find_parents('SAN')
steps = next(you_parents.index(x) + santa_parents.index(x) for x in you_parents if x in santa_parents)

print('Part Two: %d' % steps)
