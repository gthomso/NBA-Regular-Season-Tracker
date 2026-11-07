from BasketballReferenceScraper import *
from UpdateFunctions import *
from FileRWFunctions import *
import os
import cmd

# The primary function that is called from main()
# First checks pathing for if there is a text file to read from. If not it will create a new one
# No matter what path it takes it will evantually have the complete data set and will Calculate the gratness Score
def Run():
    # Seeing if txt file exists
    currentPath = os.getcwd()
    # will need to update this with the file name.
    if os.path.exists(currentPath + '\\RegularSeasonTracker.txt'):
        teamList = list()
        lastUpdate = ""
        # executes a build function to build a team list
        teamListlastUpdate = readExistFile()
        # Starts the scraping and updating process
        PullData(teamListlastUpdate)
    # For the very first cretion of seeding from power rankings.
    elif os.path.exists(currentPath + '\\SeedingPowerRanking.txt'):
        seedingFirstFile()
    return