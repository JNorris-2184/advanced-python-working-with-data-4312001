# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json

# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


def isAQuake(q):
    if q["properties"]["type"] == 'earthquake':
        return q


# 1: How many quakes are there in total?
quakes = list(filter(isAQuake, data["features"]))
print(f'Number of quakes: {len(quakes)}')

# 2: How many quakes were felt by at least 100 people?
print('Quakes felt by at least 100 people:')
print(sum(quake["properties"]["felt"] is not None and quake["properties"]["felt"] >= 100
          for quake in data["features"]))


# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
def getFelt(dataitem):
    numFelt = dataitem["properties"]["felt"]
    if (numFelt is None):
        numFelt = 0
    return numFelt


quake = max(data["features"], key=getFelt)
print(f'Location where max. # of people felt quake: {quake["properties"]["place"]}')
print(f'Number of people who felt it: {quake["properties"]["felt"]}')


# 4: Print the top 10 most significant events, with the significance value of each
def getsig(dataitem):
    significance = dataitem["properties"]["sig"]
    if (significance is None):
        significance = 0
    return significance


data['features'].sort(key=getsig, reverse=True)
for i in range(0, 10):
    print(data['features'][i]['properties']['place'])
    print(data['features'][i]['properties']['sig'])
    