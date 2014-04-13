# File name: count_selections.py
# Author: Jamie Bergen
# Date created: Apr. 3, 2014
# Date last modified: Apr. 12, 2014
# Python version: 3
# Description: Takes as input a csv file with two columns (labeled "ID" and "Selections") 
#    and produces a csv file that gives the number of times each option was selected for all IDs.

import csv
from collections import defaultdict

columns = defaultdict(list) 

with open('test.csv') as f:
    reader = csv.DictReader(f) # read rows into dictionary format
    for row in reader:
        for (k,v) in row.items():
            columns[k].append(v)

list = columns['Selections'] # generates all selections as a list of strings

newlist = []

for element in list:
    newlist.append(element.replace(' ', '').split(',')) # generates a list of lists

def count_selections(selection):
    count = 0
    for element in newlist:
        if selection in element:
            count += 1
    return count

# create a dictionary that gives the number of occurrences of each selection

selection_list = ['a', 'b', 'c', 'd']

selection_dict = {}

with open('out.csv', 'w') as f:
    print('Selection,Count', file=f)
    for g in selection_list:
        print(g + ',', count_selections(g), file=f)


