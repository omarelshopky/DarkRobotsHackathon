from flask import Flask, render_template
from components.TeamFormater import TeamFormater


app = Flask(__name__)
teamFormater = TeamFormater()



@app.route("/")
@app.route("/home")
def home():
    teams = teamFormater.orderTeams()
    return render_template('home.html', teams=teams)


@app.route("/scoreboard")
def scoreboard():
    teams = teamFormater.orderTeams()
    return render_template('scoreboard.html', title='Scoreboard', teams=teams)


@app.route("/teams-formation")
def teams_formation():
    return render_template('teams-formation.html', title='Teams Formation')


@app.route("/timeline")
def timeline():
    return render_template('timeline.html', title='Timeline')

