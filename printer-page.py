from flask import Flask, request, render_template
from datetime import datetime
import csv

app = Flask(__name__)
app.debug = True