#! /usr/bin/env python

left_list = []
right_list = []
similarity = 0

with open('input', 'r') as input_file:
  lines = input_file.readlines()
  for line in lines:
    split_line = line.split()
    left_list.append(int(split_line[0]))
    right_list.append(int(split_line[1]))

for left_num in left_list:
  count_right_occurrances = 0
  for right_num in right_list:
    if left_num == right_num:
      count_right_occurrances += 1
  similarity += left_num * count_right_occurrances

print(similarity)