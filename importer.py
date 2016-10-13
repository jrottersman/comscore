import csv
import json
import datetime
import time
import sys

from decimal import Decimal

def parse(textFile):
    with open(textFile, "rb") as f:
        reader = csv.DictReader(f, delimiter="|")
        for row in reader:
            obj = Schema(row['STB'], row['TITLE'], row['PROVIDER'], row['DATE'], row['REV'], row['VIEW_TIME'])
            fileName = "data/{0}_{1}_{2}.json".format(row['STB'],row['TITLE'],row['DATE'])
            with open(fileName, 'w') as f:
                f.write(obj.to_JSON())


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
            self.stb = self.text_length_enforcer(stb, 64)
            self.title = self.text_length_enforcer(title, 64)
            self.provider = self.text_length_enforcer(provider, 64)
            self.date = self.date_enforcer(date)
            self.rev = self.rev_formatter(rev)
            self.view_time = self.time_enforcer(view_time)
            
            
    def text_length_enforcer(self, myString, length):
        if len(myString) > length:
            raise RuntimeError("String Length violation on import")
        return myString

    def date_enforcer(self, myDate):
        try:
            correct = datetime.datetime.strptime(myDate, '%Y-%m-%d')
            return myDate
        except ValueError:
            return "{0} is an invalid date".format(myDate)

    def time_enforcer(self, myTime):
        try:
            t = time.strptime(myTime, "%H:%M")
            return myTime
        except ValueError:
            return "{0} is an invalid time please format it like HH:MM".format(myTime)

    def rev_formatter(self, rev):
       dec = Decimal(rev)
       return format(dec, '.2f')

    def to_JSON(self):
       return json.dumps(self, default=lambda o: o.__dict__,
               sort_keys=True, indent=4)

if __name__ == '__main__':
    parse(sys.argv[1])


