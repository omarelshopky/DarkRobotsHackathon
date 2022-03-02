import random
from globals import fileHandler
class TeamFormater:

    def increaseTeamCount(self, teams, team_number):
        """ Increases specific team count by one """
        teams[str(team_number)]["team-count"] += 1
        fileHandler.updateTeams(teams)

    def assignToTeam(self):
        """ Assigns player to """
        # Load current teams data
        teams = fileHandler.loadTeams()
        while True:
            randTeam = random.randint(1, fileHandler.config["TEAMS_COUNT"])
            if teams[str(randTeam)]["team-count"] != fileHandler.config["TEAMS_MAX"]:
                self.increaseTeamCount(teams, randTeam)
                break
