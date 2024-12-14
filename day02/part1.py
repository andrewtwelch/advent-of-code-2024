#! /usr/bin/env python

with open('input', 'r') as input_file:
  lines = input_file.readlines()

def list_str_to_int(old_list):
  new_list = []
  for x in old_list:
    new_list.append(int(x))
  return new_list

def is_safe(report):
  if sorted(report) == report or sorted(report) == report[::-1]:
    for i in range(1, len(report)):
      if not 1 <= abs(int(report[i]) - int(report[i - 1])) <= 3:
        return False
    return True
  else:
    return False

safe = 0

for line in lines:
  report = line.split()
  if is_safe(list_str_to_int(report)):
    safe += 1

print(safe)