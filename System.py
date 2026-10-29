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
        # Gives a option to user to use new file
        print("Player file found. Do you wish to scan existing file or create new one?")
    elif os.path.exists(currentPath + '\\SeedingPowerRanking.txt'):
        seedingFirstFile()
    return