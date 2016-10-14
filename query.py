import json
import os
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
    '''creates a list of dictionaries with the selected data'''

    values = []

    for fileName in files:
        l = {}
        with open(fileName, 'r') as f:
            json_data = json.load(f)
            for i in select:
                l[i] = json_data[i]
        
        values.append(l)

    return values

def filter_data(filter):
    '''Finds the files that have the data we want according to a filter if
    no filter is passed in it finds all files in the data directory to
    allow for them to be queried'''

    files = []
    path = 'data/'

    if filter == None:
        for fileName in os.listdir(path):
            fileName = os.path.join(path, fileName)
            files.append(fileName)
    else:
        #split the filter into the key value pair that we want to find 
        key, value = str(filter).split("=")
        
        #search for the desired key value pair in out json files
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

def main(select, order, filter):

    x = order_data(select_data(select, filter_data(filter)),order)
    
    for i in x:
        pprint(i.values())

if __name__ == '__main__':

    main(select, order, filter)
    
