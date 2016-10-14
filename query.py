import json
import os
import sys
import argparse

from collections import defaultdict
from pprint import pprint
from operator import itemgetter

def get_args():
    '''This functions parses and returns arguments passed in'''

    parser = argparse.ArgumentParser(
            description='A simple script for running selects')

    parser.add_argument(
            '-s', '--select', type=str, help='Columns to select', required=True, nargs='+')
    parser.add_argument(
            '-o', '--order', type=str, help='Columns to order by', required=False, default=None, nargs='*')
    parser.add_argument(
            '-f', '--filter', type=str, help='Column and value to filter by', required=False, default=None) 

    #gather all the arguments into an array
    args = parser.parse_args()
    #Assign args to variables
    select = args.select
    order = args.order
    filter = args.filter

    return select, order, filter

select, order, filter = get_args()



def select_data(select, files):
    #create a dict with our selected values as keys and lists to store our values
    values = []
   # path = 'data/'

    #for fileName in os.listdir(path):
     #   fileName = os.path.join(path, fileName)
    for fileName in files:
        l = {}
        with open(fileName, 'r') as f:
            json_data = json.load(f)
            for i in select:
                l[i] = json_data[i]
        
        values.append(l)

    return values

def filter_data(filter):
    #split the strings in the list
    #return the files that contain our true value
    files = []
    path = 'data/'

    if filter == None:
        for fileName in os.listdir(path):
            fileName = os.path.join(path, fileName)
            files.append(fileName)
    else:

        key, value = str(filter).split("=")

        for fileName in os.listdir(path):
            fileName = os.path.join(path, fileName)

            with open(fileName, 'r') as f:
                data = json.load(f)
                if data[key] == value:
                    files.append(fileName)
        
    return files
        
def order_data(data, order):
    if order != None:
        data = sorted(data, key = itemgetter(",".join(order)))
    return data

x = order_data(select_data(select, filter_data(filter)), order)
print(x)
#print(order_data(order, selector(select)))
