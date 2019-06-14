from flask import *
app = Flask(__name__)
import sqlite3 as sql
import pandas as pd



@app.route('/')
def home():
	return "hello world"

if __name__ == '__main__':
	app.run()
