from flask import *
app = Flask(__name__)
import sqlite3 as sql
import pandas as pd











@app.route('/')
def home():
	return render_template('home.html')
<<<<<<< HEAD

@app.route('/enternew')
def upload_csv():
	return render_template('upload.html')
 
@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
	if request.method == 'POST':
		 con = sql.connect("database.db")
		 csv = request.files['myfile']
		 file = pd.read_csv(csv)
		 file.to_sql('Earthquake', con, schema=None, if_exists='replace', index=True, index_label=None, chunksize=None, dtype=None)	  
		 con.close()
		 return render_template("result.html",msg = "Record inserted successfully")

@app.route('/list')
def list():
	con = sql.connect("database.db") 
	cur = con.cursor()
	cur.execute("select * from Earthquake")
	rows = cur.fetchall();
	con.close()
	return render_template("list.html",rows = rows)
	 
if __name__ == '__main__':
	app.run()
=======
	
if __name__ == '__main__':
  app.run()
>>>>>>> 4b655eb805ca8a81c6d4c205e3fe8a81b81c90b7
