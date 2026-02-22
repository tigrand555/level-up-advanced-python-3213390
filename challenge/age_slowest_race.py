# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians
# Assume a year has 365.25 days

import re
from datetime import datetime

def get_data():
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content

def get_event_time(line):
    """Given a line with Jennifer Rhines' race times from 10k_racetimes.txt, 
       parse it and return a tuple of (age at event, race time).
       Assume a year has 365.25 days"""
    time = line.split()[0]
    dates = re.findall(r'\d{2} \w{3} \d{4}', line)
    race_date = dates[0]
    date_of_birth = dates[1]
    race_date_obj = datetime.strptime(race_date, "%d %b %Y")
    birth_date_obj = datetime.strptime(date_of_birth, "%d %b %Y")
    age = divmod((race_date_obj - birth_date_obj).days, 365.25)
    age_str = f"{int(age[0])}y{int(age[1])}d"

    return (age_str, time)
    
def get_age_slowest_times():
    '''Return a tuple (age, race_time) where:
       age: AyBd is in this format where A and B are integers'''
    races = get_data()
    lines = races.splitlines()
    event_times = []
    for line in lines:
        if 'Jennifer Rhines' in line:
            event_times.append(get_event_time(line))
    
    # Find the slowest time and corresponding age
    slowest_time = max(event_times, key=lambda x: x[1])
    age = slowest_time[0]
    race_time = slowest_time[1]
    return (age, race_time)