import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  int_codes = [int(x) for line in file for x in line.strip().split(',')]

def run(program, noun, verb):
  program[1] = noun
  program[2] = verb
  for i in range(0, len(program), 4):
    if program[i] == 99:
      return program[0]
    a, b = program[program[i + 1]], program[program[i + 2]]
    program[program[i + 3]] = a + b if program[i] == 1 else a * b

def part_one():
   return run(int_codes[:], 12, 2)

def part_two():
  for noun in range(100):
    for verb in range(100):
      if run(int_codes[:], noun, verb) == 19690720:
        return 100 * noun + verb

print('Print One: %d' % part_one())
print('Print Two: %d' % part_two())
