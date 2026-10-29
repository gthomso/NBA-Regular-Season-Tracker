# Team function use to keep list of players, running score and
# 
class Team:
    def __init__(self) -> None:
        self.teamName = ''
        self.teamPlayers = list()
        self.teamScore = 0
        self.teamWeight = 21
        pass

    def create(name, players, score, weightOfGames):
        thisTeam = Team()
        thisTeam.TeamName = name
        thisTeam.TeamPlayers = players
        thisTeam.TeamScore = score
        thisTeam.teamWeight = weightOfGames
        return thisTeam

    def __lt__(self, other):
        return self.teamScore < other.teamScore


    teamName = ''
    teamPlayers = list()
    teamScore = 0
    teamWeight = 21