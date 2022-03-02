from flask import Flask, render_template
app = Flask(__name__)



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/teams-formation")
def teams_formation():
    return render_template('teams-formation.html', title='Team Formation')
    