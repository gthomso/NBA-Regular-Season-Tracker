# Main class used to hold most of the data that we need during this project
class Player:
    def __init__(self) -> None:
        pass
        
    # Used later for the values used in calculations.
    def __dict__(self, key):
        playerStatWeightDict = {"all_stars" : 4, "championships" : 8, 
                                "mvp" : 10, "asmvp" : 3, "dpoy" : 5,
                                "roy" : 1, "finalMVP" : 9, "allNBA" : 7,
                                "allDef" : 2, "statTitles" : 6, "careerPER" : 11,
                                "finalGreatnessScore" : 0, "runningScore" : 0}
        return playerStatWeightDict[key]
    
    # Each of the stats that we track, plus name, a running score for when pulling the data on 100
    # players, and the final Greatness Score.
    name = ''
    all_stars = 0
    championships = 0
    mvp = 0
    dpoy = 0
    roy = 0
    asmvp = 0
    finalMVP = 0
    allNBA = 0
    allDef = 0
    statTitles = 0
    careerPER = 0
    runningScore = 0
    finalGreatnessScore = 0
    