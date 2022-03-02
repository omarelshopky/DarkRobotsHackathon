from flask import Flask, render_template, request, make_response
from components.TeamFormater import TeamFormater
from components.Timeline import Timeline
from components.globals import fileHandler

app = Flask(__name__)
teamFormater = TeamFormater()
timelineHelper = Timeline()


@app.route("/")
@app.route("/home")
def home():
    teams = teamFormater.orderTeams()
    return render_template("home.html", teams=teams)


@app.route("/scoreboard")
def scoreboard():
    teams = teamFormater.orderTeams()
    return render_template("scoreboard.html", title="Scoreboard", teams=teams)


@app.route("/teams-formation", methods=["GET", "POST"])
def teams_formation():
    team = request.cookies.get('teamNum')
    isEnabled =  timelineHelper.compareWithCurrentTime(fileHandler.config["TEAM_FORMATION_START"], '>=') and timeline.compareWithCurrentTime(fileHandler.config["TEAM_FORMATION_END"], '<=')
  
    if request.method == "POST" and team == None and isEnabled:
        team = teamFormater.assignToTeam()
        
        if team == None:
            isEnabled = False
            return render_template("teams-formation.html", title="Teams Formation", team=team, isEnabled=isEnabled)
        else:
            res = make_response(render_template("teams-formation.html", title="Teams Formation", team=team, isEnabled=isEnabled))
            res.set_cookie('teamNum', str(team))
            return res
    else:
        return render_template("teams-formation.html", title="Teams Formation", team=team, isEnabled=isEnabled)

        

@app.route("/timeline")
def timeline():
    return render_template("timeline.html", title="Timeline")

