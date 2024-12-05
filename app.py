from flask import Flask, render_template
from slotmachine import *
from slotsim.main import SlotMachine

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

from botsim.discord.bot import config