from flask import *
import pandas as pd
application=app = Flask(__name__)
import sqlite3 as sql
import redis
import time
import pickle
import random
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from scipy.spatial import distance
from io import BytesIO
import base64

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
	
@app.route('/delete_i')
def delete_i():
	return render_template('d_i.html')	
	
@app.route('/deletion' , methods=['GET', 'POST'])
def deletion():
	res=[]
	
	start_t = time.time()
	w_o=[]
	
	query = "delete from Earthquake where mag >" + str(request.form['val3'])
	con = sql.connect("database.db") 
	cur = con.cursor()
	cur.execute(query)
	con.commit()
	
	cur.execute("select count(*) from Earthquake")
	rows = cur.fetchall()
	con.close()
			
	end_t=time.time()-start_t	
	return render_template("d_o.html",data = w_o ,e=end_t)	

@app.route('/names_in')
def names_in():
	return render_template('n_i.html')	

@app.route('/names_out')
def names_out():
	
	cache="mycache"

	query="select distinct net from Earthquake where net like 'n%' "
	con = sql.connect("database.db") 
	cur = con.cursor()
	cur.execute(query)
	rows =cur.fetchall();
	con.close()
	
	start_t = time.time()
	
	for i in range(100):
	
		ran_num=random.randint(0,len(rows)-1)
		#print (ran_num)
		if r.exists(cache+str(rows[ran_num])):
			t="with"
			temp_res = pickle.loads(r.get(cache+str(rows[ran_num])))
			#w_o.append(t)
			
		else:	
			v=str(rows[ran_num])
			#print(type(v[2:4]))
			query = "select * from Earthquake where net = '"+v[2:4]+"'"       
			print(query)
			t="without"
			#w_o.append(t)
			con = sql.connect("database.db") 
			cur = con.cursor()
			cur.execute(query)
			temp_res = cur.fetchall()
			#if rows!= None:
				#res.append(rows)
			r.set(cache+str(rows[ran_num]),pickle.dumps(temp_res))
			con.close()
	#r.set(cache,pickle.dumps(rows))
	end_t=time.time()-start_t
		
	return render_template("n_o.html",e=end_t)	

def convert_fig_to_html(fig):
	
	figfile = BytesIO()
	plt.savefig(figfile, format='png')
	figfile.seek(0)  # rewind to beginning of file
	
	#figdata_png = base64.b64encode(figfile.read())
	figdata_png = base64.b64encode(figfile.getvalue())
	return figdata_png

@app.route('/clustering')
def clustering():	

	query = "SELECT latitude,longitude FROM Earthquake "
	con = sql.connect("database.db") 
	cur = con.cursor()
	cur.execute(query)
	rows = cur.fetchall()
	y=pd.DataFrame(rows)
	
	k=KMeans(n_clusters=5,random_state=0).fit(y)
	c=k.cluster_centers_
	l=k.labels_
	X= y.dropna()
	#print(X[0])	
	fig=plt.figure()
	plt.scatter(X[0],X[1],c=l)
	plt.scatter(c[:, 0], c[:, 1], c='red', s=200, marker='+')
	plot=convert_fig_to_html(fig)
	#print(X[:,0])
	#plt.show()
	#fig.savefig('static/img.png')
	#print(k.cluster_centers_)

	return render_template("clus_o.html",data=plot.decode('utf8'))

if __name__ == '__main__':
	app.run()