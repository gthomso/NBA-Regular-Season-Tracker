# Main class used to hold players value data
class Player:
    def __init__(self) -> None:
        pass

    def __init__(self, team):
        self.team = team
        pass  
    # Used later for the values used in calculations.
    
    # Each of the stats that we track, plus name, a running score for when pulling the data on 100
    # players, and the final Greatness Score.
    ValueScore = 0
    Team = ''
    