import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  program = [int(x) for line in file for x in line.strip().split(',')]

pc = 0
while pc < len(program):
  op, modes = program[pc] % 100, [(program[pc] // x) % 10 for x in (100, 1000, 10000)]
  param = lambda n: program[pc + n] if modes[n - 1] else program[program[pc + n]]
  if op == 99:
    break
  if op in (1, 2):
    program[program[pc + 3]] = param(1) + param(2) if op == 1 else param(1) * param(2)
    pc += 4
  elif op == 3:
    program[program[pc + 1]] = int(input('Input a number: '))
    pc += 2
  elif op == 4:
    print(param(1))
    pc += 2
  elif op in (5, 6):
    pc = param(2) if bool(param(1)) != (op == 6) else pc + 3
  elif op == 7: 
    program[program[pc + 3]] = param(1) < param(2)
    pc += 4
  elif op == 8:
    program[program[pc + 3]] = param(1) == param(2)
    pc += 4
