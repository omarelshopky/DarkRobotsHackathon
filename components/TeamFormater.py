import random
from components.globals import fileHandler

class TeamFormater:

    def increaseTeamCount(self, teams, team_number):
        """ Increases specific team count by one """
        teams[str(team_number)]["team-count"] += 1
        fileHandler.updateTeams(teams)

    def assignToTeam(self):
        """ Assigns player to """
        # Load current teams data
        teams = fileHandler.loadTeams()
        
        # Check if there an empty teams
        count = 0
        for team in teams:
            if teams[str(team)]["team-count"] == fileHandler.config["TEAMS_MAX"]:
                count += 1

        if count == len(teams):
            return None

        while True:
            randTeam = random.randint(1, fileHandler.config["TEAMS_NUMBER"])
            if teams[str(randTeam)]["team-count"] != fileHandler.config["TEAMS_MAX"]:
                self.increaseTeamCount(teams, randTeam)
                return randTeam
    
    def orderTeams(self):
        teams = fileHandler.loadTeams()
        t = []
        for team in teams:
            t.append([teams[team]['points'], teams[team]['team-name']])
            
        t.sort(reverse=True)
        return t
    
