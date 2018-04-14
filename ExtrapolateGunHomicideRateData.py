year_counts = dict()
for year in years:
    if year in year_counts:
        year_counts[year] += 1
    else:
        year_counts[year] = 1

dates = [datetime.datetime(year=int(row[1]), month=int(row[2]), day=1) for row in data]
date_counts = dict()
for date in dates:
    if date in date_counts:
        date_counts[date] += 1
    else:
        date_counts[date] = 1

sexes = [row[5] for row in data]
sex_counts = dict()
for sex in sexes:
    if sex in sex_counts:
        sex_counts[sex] += 1
    else:
        sex_counts[sex] = 1

races = [row[7] for row in data]
race_counts = dict()
for race in races:
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1

f = open('census.csv', 'r')
census = list(csv.reader(f))
f.close()

mapping = {
    'Asian/Pacific Islander': 674625,
    'Black': 40250635,
    'Native American/Native Alaskan': 3739506 + 15159516,
    'Hispanic': 44618105,
    'White': 197318956
}

race_per_hundredk = dict()
for race in race_counts:
    race_per_hundredk[race] = (race_counts[race] / mapping[race]) * 100000

intents = [row[3] for row in data]
races = [row[7] for row in data]

homicide_race_counts = dict()

for i, race in enumerate(races):
    if intents[i] == 'Homicide':
        if race in homicide_race_counts:
            homicide_race_counts[race] += 1
        else:
            homicide_race_counts[race] = 1

for race in race_counts:
    homicide_race_counts[race] = (homicide_race_counts[race] / mapping[race]) * 100000

print(homicide_race_counts)
