from itertools import groupby

passwords_1 = [
  str(code) for code in range(172851, 675869 + 1)
  if sum([10 * int(a <= b) + int(a == b) for a, b in zip(str(code // 10), str(code % 100000))]) > 50
]

passwords_2 = [password for password in passwords_1 if 2 in [len(list(it)) for ch, it in groupby(password)]]

print('Part One: %d' % len(passwords_1))
print('Part Two: %d' % len(passwords_2))
