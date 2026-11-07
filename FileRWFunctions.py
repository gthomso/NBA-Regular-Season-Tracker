# This python file is concerned with reading and writing
# to the RegularSeasonTracker txt file.
import os
import string
import datetime
#importing Team only to sort when seeding.
from Team import *
from Player import *

# Process called when first seeding is needed
def seedingFirstFile():
    # opening the seed power ranking
    with open("SeedingPowerRanking.txt", "r", encoding="utf-8") as file:
        # Reading file lines once at a time and creating the team.
        file.readline()
        teamList = list()
        while True:
            line = file.readline()
            if not line:
                file.close()
                break
            splitLine = line.split(';')
            lineTeam = seedingLineOrganization(splitLine)
            teamList.append(lineTeam)
    writingFirstFile(teamList)
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

# Called when the first line for a team is called.
def teamStatOrganization(splitLine:list):
    partialLine = splitLine.split('\t')
    teamLine = partialLine[0].split(' ',1)[1]
    nLine = partialLine[1].split(' ')[2]
    scoreLine = partialLine[2].split(' ')[1].strip("\n")
    retList = [teamLine, nLine, scoreLine]
    return retList

# Called whenever the players line is called.
def playerOrganization(splitLine:list):
    retPlayer = Player()
    retPlayer = splitLine[1]
    return retPlayer


def writingFirstFile(teamList):
    teamList.sort(reverse=True)
    index = 1
    f = open("RegularSeasonTracker.txt", "w")
    f.write("October/19/2026\n")
    for eachTeam in teamList:
        f.write(str(index)+" "+eachTeam.teamName+"\tN weight: "+str(eachTeam.teamWeight)+"\tScore: "+str(eachTeam.teamScore)+"\n")
        index += 1
    f.close()
    return

def readExistFile():
    # opening the seed power ranking
    with open("RegularSeasonTracker.txt", "r", encoding="utf-8") as file:
        # Reading file lines once at a time and creating the team.
        lastDate=file.readline()
        teamList = list()
        line = file.readline()
        while True:
            if not line:
                file.close()
                break
            if(line[0].isdigit()):
                teamStat=teamStatOrganization(line)
                line = file.readline()
                if not line:
                    file.close()
                    break
                players = list()
                while(not line[0].isdigit()):
                    playerStat = playerOrganization(line)
                    players.append(playerStat)
                    line = file.readline()
            lineTeam = teamConstruction(teamStat,players)
            teamList.append(lineTeam)
    # Returns a tuple to get access to both of these.
    return (teamList,lastDate)

#writing the update and sorted 
def writeUpdatedTeamFile(teamList):
    f = open("RegularSeasonTracker.txt", "w")
    currentDate = datetime()
    for eachTeam in teamList:
        f.write(str(index)+" "+eachTeam.teamName+"\tN weight: "+str(eachTeam.teamWeight)+"\tScore: "+str(eachTeam.teamScore)+"\n")
        for eachPlayer in teamList.teamPlayers:
            f.write("\t- "+eachPlayer.PlayerName+"\tValueScore"+eachPlayer.ValueScore+"\n")
        index += 1
    f.close()
    return

def writeUpdatedPlayerFile(teamList):
    f = open("PlayerRankings.txt", "w")
    teamList.sort(reversed)
    for eachTeam in teamList:
        f.write(str(index)+" "+eachTeam.teamName+"\tN weight: "+str(eachTeam.teamWeight)+"\tScore: "+str(eachTeam.teamScore)+"\n")
        index += 1
    f.close()
    return

def teamConstruction(teamStat, players):
    tempTeam = Team()
    setattr(tempTeam, 'teamName', teamStat[0])
    setattr(tempTeam, 'teamWeight', teamStat[1])
    setattr(tempTeam, 'teamScore', teamStat[2])
    setattr(tempTeam, 'teamPlayers', players)
    return tempTeam
