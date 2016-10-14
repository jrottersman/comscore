import csv
import json
import datetime
import time
import sys
import os
import re

from decimal import Decimal

def parse(textFile):
    if os.path.getsize(textFile) > 0 :
        with open(textFile, "rb") as f:
            reader = csv.DictReader(f, delimiter="|")
            for row in reader:
                obj = Schema(row['STB'], row['TITLE'], row['PROVIDER'], row['DATE'], row['REV'], row['VIEW_TIME'])
                fileName = "data/{0}_{1}_{2}.json".format(row['STB'],row['TITLE'],row['DATE'])
                with open(fileName, 'w') as f:
                    f.write(obj.to_JSON())
    else: 
        print("{0} is empty".format(textFile))

class Schema(object):
    """This checks the data integerity of our sample data to make sure that it complies with out schema which has the following properties:

    Attributes:
        STB: 64 char text (the set top box id where the media asset was viewed)
        Title: 64 char text (the title of media asset)
        Provider: 64 char text (the distrubator of the media asset)
        Date: a date in YYYY-MM-DD form (the local date the content was leased)
        REV: dollars and cents price in a form like this 8.45 (price paid)
        VIEW_TIME - time in hours:minutes like 1:45 (the amount of time the asset was played
        """

    def __init__(self, stb, title, provider, date, rev, view_time):
            self.STB = self.text_length_enforcer(stb, 64)
            self.TITLE = self.text_length_enforcer(title, 64)
            self.PROVIDER = self.text_length_enforcer(provider, 64)
            self.DATE = self.date_enforcer(date)
            self.REV = self.rev_enforcer(rev)
            self.VIEW_TIME = self.time_enforcer(view_time)
            
            
    def text_length_enforcer(self, myString, length):
        if len(myString) > length:
            raise RuntimeError("String Length violation on import")
        elif len(myString) == 0:
            raise RuntimeError("row's can not be null")
        return myString

    def date_enforcer(self, myDate):
        try:
            correct = datetime.datetime.strptime(myDate, '%Y-%m-%d')
            return myDate
        except ValueError:
            raise RuntimeError("{0} is an invalid date date must be in YYYY-mm-dd form".format(myDate))

    def time_enforcer(self, myTime):
        try:
            t = time.strptime(myTime, "%H:%M")
            return myTime
        except ValueError:
            raise RuntimeError("{0} is an invalid time please format it like HH:MM".format(myTime))

    def rev_enforcer(self, rev):
        regex = r"[0-9]{1,}.[0-9]{2}$"
        if re.match(regex, rev) is not None:
            return rev
        else:
            raise RuntimeError("{0} is not valid please format Rev like 00.00".format(rev))

    def to_JSON(self):
       return json.dumps(self, default=lambda o: o.__dict__,
               sort_keys=True, indent=4)

if __name__ == '__main__':
    parse(sys.argv[1])


