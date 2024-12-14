#! /usr/bin/env python

import re

expression = r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))'

with open('input', 'r') as input_file:
  memory = input_file.read()

matches = re.findall(expression, memory)

total = 0
enabled = True

for calc in matches:
  if calc == 'do()':
    enabled = True
  elif calc == 'don\'t()':
    enabled = False
  elif enabled:
    split = calc[4:-1].split(',')
    total += int(split[0]) * int(split[1])

print(total)