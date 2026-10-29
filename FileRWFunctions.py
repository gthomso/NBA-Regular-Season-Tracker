# This python file is concerned with reading and writing
# to the RegularSeasonTracker txt file.
import os
import string
#importing Team only to sort when seeding.
from Team import *

#Creating global team list for the seeding process
teamList = list()

# Process called when first seeding is needed
def seedingFirstFile():
    # opening the seed power ranking
    with open("SeedingPowerRanking.txt", "r", encoding="utf-8") as file:
        # Reading file lines once at a time and creating the team.
        file.readline()
        while True:
            line = file.readline()
            if not line:
                file.close()
                break
            splitLine = line.split(';')
            lineTeam = seedingLineOrganization(splitLine)
            teamList.append(lineTeam)
    writingFirstFile()
    return

# Taking the splitlines and organizing them into global team list variable
def seedingLineOrganization(splitLine:list):
    teamLine = splitLine[0]
    scoreLine = splitLine[1].split(':')[1]
    nLine = splitLine[2].split(':')[1].split('\n')[0]
    thisTeam = Team()
    setattr(thisTeam, 'teamName', teamLine)
    thisTeam.teamName = teamLine
    thisTeam.teamScore = float(scoreLine)
    thisTeam.teamWeight = int(nLine)
    return thisTeam



def writingFirstFile():
    teamList.sort(reverse=True)
    index = 1
    f = open("RegularSeasonTracker.txt", "w")
    for eachTeam in teamList:
        f.write(str(index)+" "+eachTeam.teamName+"\tN weight: "+str(eachTeam.teamWeight)+"\tScore: "+str(eachTeam.teamScore)+"\n")
        index += 1
    f.close()
    return
