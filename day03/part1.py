#! /usr/bin/env python

import re

expression = r'mul\(\d+,\d+\)'

with open('input', 'r') as input_file:
  memory = input_file.read()

matches = re.findall(expression, memory)

total = 0

for calc in matches:
  split = calc[4:-1].split(',')
  total += int(split[0]) * int(split[1])

print(total)