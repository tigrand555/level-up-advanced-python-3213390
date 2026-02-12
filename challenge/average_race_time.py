# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import datetime

def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content

def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()
    rhines_times = re.findall(r'(\d+:\d+\.?\d+)\s+Jennifer Rhines', races)
    return rhines_times

def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    total = datetime.timedelta()
    for racetime in racetimes:
        try:
            mins, secs, ms = re.split(r'[:.]', racetime)
            print(mins, secs, ms)
            total += datetime.timedelta(minutes=int(mins), seconds=int(secs), milliseconds=int(ms))
        except ValueError:
            mins, secs = re.split(r'[:.]', racetime)
            total += datetime.timedelta(minutes=int(mins), seconds=int(secs))
    return f'{total / len(racetimes)}'[2:-5]

