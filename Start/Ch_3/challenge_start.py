# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import datetime

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD
def getsig(q):
    significance = q["properties"]["sig"]
    if significance is not None:
        return significance


def getdate(q):
    occurdate = q["properties"]["date"]
    if occurdate is not None:
        return occurdate


def simplequake(q):
    return {
        "place": q["properties"]["place"],
        "mag": q["properties"]["mag"],
        "link": q["properties"]["url"],
        "felt": q["properties"]["felt"],
        "date": str(datetime.date.fromtimestamp(int(q["properties"]["time"] / 1000)))
    }


header = ["Magnitude", "Place", "Felt Reports", "Date", "Map link"]
rows = []
data['features'].sort(key=getsig, reverse=True)

quakes = []

for i in range(0, 40):
    quakes.append(data['features'][i])

quakes = list(map(simplequake, quakes))

for quake in quakes:
    rows.append([quake["mag"],
                 quake["place"],
                 quake["felt"],
                 quake["date"],
                 quake["link"]])

with open("sigquakes.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(header)
    writer.writerows(rows)
