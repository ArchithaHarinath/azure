from flask import *
import pandas as pd
application=app = Flask(__name__)
import sqlite3 as sql
import redis
import time
import _pickle as pickle



myHostname = "architha.redis.cache.windows.net"
myPassword = "0D0U2S4PfqMI7vkbaQ82TUNJB2jSYW2xpWawpgFPrHk="

r = redis.StrictRedis(host=myHostname,port=6380, db=0, password=myPassword, ssl=True)


@app.route('/')
def home():
	return render_template('home.html')
	
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
	start_t=time.time()
	con = sql.connect("database.db") 
	cur = con.cursor()
	cur.execute("select * from Earthquake")
	rows = cur.fetchall();
	con.close()
	end_t=time.time()-start_t
	return render_template("list.html",rows = rows,e=end_t)
	
if __name__ == '__main__':
	app.run()