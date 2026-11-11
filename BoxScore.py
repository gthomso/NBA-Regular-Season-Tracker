# Team function use to keep list of players, running score and
# 
class BoxScore:
    def __init__(self) -> None:
        pass

    def __lt__(self, other):
        return self.teamScore < other.teamScore


    winner = ""
    loser = ""
    ImpactPlayersList = list()