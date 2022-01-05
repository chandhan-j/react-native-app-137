import pandas as pd
import csv

df = pd.read_csv("Stars.csv")

df.drop(['Unnamed: 0'], axis = 1, inplace = True)

name = df["Name"].tolist()

mass = df["Mass"].tolist()

radius = df["Radius"].tolist()

distance = df["Distance"].tolist()

gravity = df["Gravity"].tolist()

final_star_list = []

tempDict = {}

for i in range(0, len(name)):
    tempDict["Name"] = name[i]
    tempDict["distance"] = distance[i]
    tempDict["radius"] = radius[i]
    tempDict["mass"] = mass[i]
    tempDict["gravity"] = gravity[i]

    final_star_list.append(tempDict)
    tempDict = {}

print(final_star_list)

with open('dataProject.csv', 'w', encoding = 'utf8') as f:
    writer = csv.writer(f)
    writer.writerow(final_star_list)