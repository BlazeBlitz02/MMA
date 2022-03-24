import numpy as np
import pandas as pd

filePath = "sampleOutput.csv"
groundTruthFilePath = "groundTruth.csv"

results = pd.read_csv(filePath)
groundTruth = pd.read_csv(groundTruthFilePath)

totalPoints = 3 * len(groundTruth['Video'])

points = 0

for video in groundTruth['Video']:
    trueLocation = groundTruth.loc[groundTruth['Video'] == video]['Location'][0]
    row = results.loc[results['Video'] == video]
    
    if row['Guess1'][0] == trueLocation:
        points += 3
        print("Guess 1 was correct for video {}".format(video))
    elif row['Guess2'][0] == trueLocation:
        points += 2
        print("Guess 2 was correct for video {}".format(video))
    elif row['Guess3'][0] == trueLocation:
        points += 1
        print("Guess 3 was correct for video {}".format(video))
    else:
        print("No guess was correct for video {}".format(video))
        

print("Total points: {} out of {}, or {}%".format(points, totalPoints, points*100/totalPoints))