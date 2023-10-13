from flask import Flask, render_template
app = Flask(__name__)

import os
import json

os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open("Sixers.json") as jsonFile:
    jsonData = jsonFile.read()

sixers = json.loads(jsonData)

@app.route('/')
def Kevin():
    return render_template("kevin.html")

@app.route('/Sixers/')
def SixerInfo():
    return render_template("sixers.html", players=sixers)

if __name__ == "__main__":
    app.run(debug=True)

