import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  wires = [line.strip().split(',') for line in file]

points = [{}, {}]
for n, steps in enumerate(wires):
  x = y = d = 0
  for step in steps:
    for _ in range(int(step[1:])):
      x += 1 if step[0] == 'R' else -1 if step[0] == 'L' else 0
      y += 1 if step[0] == 'U' else -1 if step[0] == 'D' else 0
      d += 1
      points[n][(x, y)] = d

intersections = set(points[0]).intersection(set(points[1]))

part_one = min([abs(x[0]) + abs(x[1]) for x in intersections])
part_two = min([points[0][x] + points[1][x] for x in intersections])

print('Part One: %d' % part_one)
print('Part Two: %d' % part_two)
