from flask import *
import pandas as pd
application=app = Flask(__name__)
import sqlite3 as sql
import redis
import time
import pickle
import random


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
	
	cache="mycache"
	start_t = time.time()
	query="select * from Earthquake"
	if r.exists(cache):
		t="with"
		print(t)
		isCache = 'with Cache'
		
		rows = pickle.loads(r.get(cache))
		end_t = time.time()-start_t
		r.delete(cache)
		
	else:
		t="without"
		print(t)
		con = sql.connect("database.db") 
		cur = con.cursor()
		cur.execute(query)
		rows = cur.fetchall();
		con.close()
		r.set(cache,pickle.dumps(rows))
		end_t=time.time()-start_t
		
	return render_template("list.html",rows = rows,e=end_t, t=t)

@app.route('/c_i')
def c_i():
	return render_template('c_i.html')
	
@app.route('/mag_list' , methods=['GET', 'POST'])
def mag_list():
	res=[]
	cache="mycache"
	start_t = time.time()
	w_o=[]
	for i in range(100):
		ran_num="{:.2f}".format(random.uniform(-2,8))
		print (ran_num)
		if r.exists(cache+str(ran_num)):
			t="with"
			rows = pickle.loads(r.get(cache+str(ran_num)))
			w_o.append(t)
		else:	
			query = "select * from Earthquake where mag>" + str(ran_num)
			t="without"
			w_o.append(t)
			con = sql.connect("database.db") 
			cur = con.cursor()
			cur.execute(query)
			rows = cur.fetchall()
			if rows!= None:
				res.append(rows)
			r.set(cache+str(ran_num),pickle.dumps(rows))
			con.close()
	print(w_o)		
	end_t=time.time()-start_t	
	return render_template("mag_greater.html",data = w_o ,e=end_t)	

if __name__ == '__main__':
	app.run()