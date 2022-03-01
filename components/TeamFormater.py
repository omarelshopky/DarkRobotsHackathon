import FileHandler
import random

class TeamFormater:
    def __init__(self):
        self.fileHandler = FileHandler()

    def increaseTeamCount(self, teams, team_number):
        """ Increases specific team count by one """
        teams[str(team_number)]["team-count"] += 1
        self.fileHandler.updateTeams(teams)

    def assignToTeam(self):
        """ Assigns player to """
        # Load current teams data
        teams = self.fileHandler.loadTeams()
        while True:
            randTeam = random.randint(1, self.fileHandler.config["TEAMS_COUNT"])
            if teams[str(randTeam)]["team-count"] != self.fileHandler.config["TEAMS_MAX"]:
                self.increaseTeamCount(teams, randTeam)
                break
