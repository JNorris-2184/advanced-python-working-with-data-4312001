# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

show_expected_result = False
show_hints = False

import json
from collections import Counter


def qtype(q):
    return q['properties']['type'] is not None


def simplify(q):
    return q["properties"]["type"]


# open the data file and load the JSON
def get_event_classification():
    with open("../../30DayQuakes.json", "r") as datafile:
        data = json.load(datafile)

    # categorize each event and count each one
    events = list(filter(qtype, data['features']))
    eventtypes = list(map(simplify, events))
    c1 = Counter(eventtypes)

    # return the result
    print(c1.most_common(6))


get_event_classification()