#! /usr/bin/env python

left_list = []
right_list = []
distance = 0

with open('input', 'r') as input_file:
  lines = input_file.readlines()
  for line in lines:
    split_line = line.split()
    left_list.append(int(split_line[0]))
    right_list.append(int(split_line[1]))

left_list.sort()
right_list.sort()

for i in range(len(left_list)):
  distance += abs(left_list[i] - right_list[i])

print(distance)