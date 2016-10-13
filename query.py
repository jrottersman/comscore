import json
import os
import sys
import argparse

def get_args():
    '''This functions parses and returns arguments passed in'''

    parser = argparse.ArgumentParser(
            description='A simple script for running selects')

    parser.add_argument(
            '-s', '--select', type=str, help='Columns to select', required=True, nargs='+')
    parser.add_argument(
            '-o', '--order', type=str, help='Columns to order by', required=False, default=None, nargs='*')
    parser.add_argument(
            '-f', '--filter', type=str, help='Column and value to filter by', required=False, default=None, nargs='*')

    #gather all the arguments into an array
    args = parser.parse_args()
    #Assign args to variables
    select = args.select
    order = args.order
    filter = args.filter

    return select, order, filter

select, order, filter = get_args()
print("select the following: [%s]\n" % select)
print("ordered by: [%s]\n" % order)
print("filtered withL %s\n" % filter)

#def run():
 #   path = 'data/'
#
 #   for fileName in os.listdir(path):
  #      with open(fileName, 'w'):
   #         select():

#def init_select(*arg):
 #   for i in range(len(arg)):


#def select(*arg):
 #   for i in range(len(arg)):

