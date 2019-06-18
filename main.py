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
from math import * 
from math import radians

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
		file.to_sql('Earth', con, schema=None, if_exists='replace', index=True, index_label=None, chunksize=None, dtype=None)	  
		con.close()
	return render_template("result.html",msg = "Record inserted successfully")

@app.route('/list')
def list():
	
	cache="mycache"
	start_t = time.time()
	query="select * from Earthquake "
	
	
	#query="select County from Countries where state=(select FULL from Statef where CODE='AK')"
	
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
		rows = str(cur.fetchall());
		con.close()
	
		r.set(cache,pickle.dumps(rows))
		end_t=time.time()-start_t
	
	
	return render_template("list.html",data = rows)
	#return render_template("list.html",rows = rows,e=end_t, t=t),data = rows

@app.route('/magrange_i')
def magrange_i():
	return render_template('mag_i.html')
	
@app.route('/mag_list' , methods=['GET', 'POST'])
def mag_list():
	
	if request.method=='POST':
		mag_v1 = int(request.form["val1"])
		mag_v2 = int(request.form["val2"])
		
		query = "select place,time,mag from Earthquake where latitude >= ' " + str(mag_v1)+ " 'and latitude <=' " + str(mag_v2)+ " ' " 
		con = sql.connect("database.db") 
		cur = con.cursor()
		cur.execute(query)
		rows = cur.fetchall()
		#print (rows)
		
		'''
		res=[]
		cache="mycache"
		cache_t=0
		uncache_t=0
		cc=0
		uc=0
		w_o=[]
		st=time.time()
		for i in range(1000):
			ran_num="{:.2f}".format(random.uniform(mag_v1,mag_v2))
			#print (ran_num)
			if r.exists(cache+str(i)):
				#t="with"
				start_t = time.time()
				#rows = pickle.loads(r.get(cache+str(ran_num)))
				rows=r.get(cache+str(i))
				end_t=time.time()-start_t
				cache_t+=end_t
				cc+=1
				#w_o.append(t)
			else:	
				start_t = time.time()
				query = "select * from Earthquake where mag>" + str(ran_num)
				t="without"
				w_o.append(t)
				con = sql.connect("database.db") 
				cur = con.cursor()
				cur.execute(query)
				#rows = cur.fetchall()
				end_t=time.time()-start_t
				uncache_t+=end_t
				#r.set(cache+str(ran_num),pickle.dumps(rows))
				r.set(cache+str(i),1)
				uc+=1
				con.close()
		#print(w_o)		
		et=time.time()-st	
		'''
	return render_template("mag_greater.html", data=rows)	
	#return render_template("mag_greater.html",un=uncache_t,c=cache_t,e=et)	
	
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
	return render_template("d_o.html",data=rows,e=end_t)	

@app.route('/names_in')
def names_in():
	return render_template('n_i.html')	

@app.route('/names_out',methods=['GET', 'POST'])
def names_out():
	
	if request.method=='POST':
	
		cache="mycache"
		chara = request.form["val1"]
		query="select distinct net from Earthquake where net like '"+chara+"%' "
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
	
@app.route('/lat_i')
def lat_i():
	return render_template('lat_input.html')		
	
	
@app.route('/select_lat',methods=['GET', 'POST'])
def select_lat():

	rows = []
	magnitudes=[]
	if request.method=='POST':
		radius = 6373.0
		res=[]
		start_t = time.time()
		
		cache="mycache"
		
		if r.exists(cache+str(rows[ran_num])):
			t="with"
			temp_res = pickle.loads(r.get(cache+str(rows[ran_num])))
		
		else:
			
			query = " SELECT * FROM  Earthquake "
			con = sql.connect("database.db") 
			cur = con.cursor()
			cur.execute(query)
			#rows =cur.fetchall()
			con.close()
			for row in rows:
				lat1 = radians(float(row[2]))
				lon1 = radians(float(row[3]))
				dist_lat = lat1-radians(float(request.form['val1']))
				dist_lon = lon1 -radians(float(request.form['val2']))
				formula =abs( sin(dist_lat / 2)*2 + cos(radians(float(request.form['val1']))) * cos(lat1) * sin(dist_lon / 2)*2)
				ans = 2*atan2(sqrt(formula), 1-sqrt(formula))
				distance = float(radius*ans)
				
				val1=request.form['val3']
				if distance <= (float(val1)):
					res.append(row[5])
		end_t=time.time()
	return render_template("lat_out.html", end=end_t-start_t)


def convert_fig_to_html(fig):
	
	figfile = BytesIO()
	plt.savefig(figfile, format='png')
	figfile.seek(0) 
	figdata_png = base64.b64encode(figfile.getvalue())
	return figdata_png

@app.route('/clustering')
def clustering():	

	query = "SELECT latitude,longitude FROM Earthquake "
	#query = "SELECT mag FROM Earthquake "
	con = sql.connect("database.db") 
	cur = con.cursor()
	cur.execute(query)
	rows = cur.fetchall()
	y=pd.DataFrame(rows)
	X= y.dropna()
	k=KMeans(n_clusters=5,random_state=0).fit(X)
	
	c=k.cluster_centers_
	l=k.labels_
		
	fig=plt.figure()
	plt.scatter(X[0],X[1],c=l)
	print(c[:,0])
	plt.scatter(c[:, 0], c[:, 1], c='y', s=100, marker='x')
	plt.title('Clusters based on latitude and longitude')
	plt.xlabel('latitude')
	plt.ylabel('longitude')
	plot=convert_fig_to_html(fig)
	
	return render_template("clus_o.html",data=plot.decode('utf8'))

if __name__ == '__main__':
	app.run()