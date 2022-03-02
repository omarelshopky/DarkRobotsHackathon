from flask import Flask, render_template
app = Flask(__name__)



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/scoreboard")
def scoreboard():
    return render_template('scoreboard.html', title='Scoreboard')


@app.route("/teams-formation")
def teams_formation():
    return render_template('teams-formation.html', title='Teams Formation')


@app.route("/timeline")
def timeline():
    return render_template('timeline.html', title='Timeline')


    