import json

class FileHandler:
    config = []

    def __init__(self):
        self.loadConfig()

    def loadConfig(self):
        """ Loads the config from json file """
        with open("config.json") as f:
            FileHandler.config = json.load(f)

    def loadTeams(self):
        """ Loads the teams data from json file """
        with open(self.config["TEAMS_FILE"]) as f:
            return json.load(f)
    
    def updateTeams(self, newTeams):
        """ Updates teams data with new json """
        with open(self.config["TEAMS_FILE"], "w") as f:
            json.dump(newTeams, f)

