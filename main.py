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
		file.to_sql('Vote', con, schema=None, if_exists='replace', index=True, index_label=None, chunksize=None, dtype=None)	  
		con.close()
	return render_template("result.html",msg = "Record inserted successfully")

@app.route('/list')
def list():
	
	var1=500
	var2=1000
	var3=50000
	query = "select StateName from Vote where TotalPop BETWEEN ' " + str(var1)+ " 'and ' " + str(var2)+ " ' " 
	#query="select * from Vote"  and TotalPop <=' " +str(var2)+" '
	con = sql.connect("database.db") 
	cur = con.cursor()
	cur.execute(query)
	rows = str(cur.fetchall());
	con.close()
	
	query = "select StateName from Vote where TotalPop BETWEEN ' " + str(var1)+ " 'and ' " + str(var2)+ " ' " 
	#query="select * from Vote"  and TotalPop <=' " +str(var2)+" '
	con = sql.connect("database.db") 
	cur = con.cursor()
	cur.execute(query)
	rows1 = str(cur.fetchall());
	con.close()
	
	
	#print(rows)
	
	return render_template("list.html",data = rows , data1=rows1)
	#return render_template("list.html",rows = rows,e=end_t, t=t),data = rows

@app.route('/magrange_i')
def magrange_i():
	return render_template('mag_i.html')
	
@app.route('/mag_list' , methods=['GET', 'POST'])
def mag_list():
	
	if request.method=='POST':
		mag_v1 = int(request.form["val1"])
		mag_v2 = int(request.form["val2"])
		temp=[]
		time1=[]
		time2=[]
		cache="mycache"
		full_start=time.time()
		for i in range(int(request.form["val3"])):
			if r.exists(cache+str(i)):
				start_t = time.time()
				rows = pickle.loads(r.get(cache+str(i)))
				temp.append(rows)
				end_t=time.time()-start_t
				time2.append(end_t)
				
			else:
				res=[]
				ran_num="{:.3f}".format(random.uniform(mag_v1,mag_v2))
				ran_num2="{:.3f}".format(random.uniform(mag_v1,mag_v2))
				st=time.time()
				query = "select count(*) from Earthquake where latitude >= ' " + str(ran_num)+ " 'and latitude <=' " + str(ran_num2)+ " ' " 
				con = sql.connect("database.db") 
				cur = con.cursor()
				cur.execute(query)
				rows = cur.fetchall()
				res.append(rows)
				res.append(ran_num)
				res.append(ran_num2)
				temp.append(res)
				r.set(cache+str(i),pickle.dumps(res))
				et=time.time()-st
				time1.append(et)
		
		end_time=time.time()-full_start
		
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
	return render_template("mag_greater.html", data=temp , time2 =end_time)	
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





	

	'''
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
	n=[]
	m=[]
	label=pd.DataFrame(l)
	#get count of number of points in each cluster 
	for i in range(5):
		n.append(len(label.index[label[0]==i].tolist()))
		
	# eucledian distance 
	for i in  range(len(c)):
		temp=[]
		for j in range(0,len(c)):
			temp.append(distance.euclidean(c[i],c[j]))
		m.append(temp)
		
	print (m)
	'''
	'''
	for i in  range(len(c)):
		temp=[]
		t = "c"+str(i)
		m.append(t)
		for j in range(0,len(c)):
			if i!=j :
				temp.append(distance.euclidean(c[i],c[j]))
		m.append(temp)
	
	#print(n)
	print(m)
	'''
	#elbow method
	'''
	Ks = range(2, 10)
	km = [KMeans(n_clusters=i) for i in Ks]
	score = [km[i].fit(X).score(X)**2 for i in range(len(km))]
	y = plt.plot(Ks,score)
	'''

	plt.show()
	
	

	fig=plt.figure()
	plt.scatter(X[0],X[1],c=l)
	#print(c[:,0])
	plt.scatter(c[:, 0], c[:, 1], c='y', s=100, marker='x')
	plt.title('Clusters based on latitude and longitude')
	plt.xlabel('latitude')
	plt.ylabel('longitude')
	plot=convert_fig_to_html(fig)
	return render_template("clus_o.html",data=plot.decode('utf8'))

@app.route('/pie_i')
def pie_i():
	return render_template('pie_input.html')	

@app.route('/pie_chart' ,methods=['GET', 'POST'])
def pie_chart():
	
	if request.method=='POST':	
	
		'''
		n = int(request.form["val1"])
		n2= int(request.form["val2"])
		x=[]
		y=[]
		i=n
		for i in range (n2):

			t=(i*i)+1
			x.append(t)
			y.append(i)
		
		
		fig = plt.figure()
		plt.plot(y,x ,marker ='o',color='r',markeredgecolor='b')
		plt.title('x=(y*y)+1')
		plt.xlabel('y value')
		plt.ylabel('x value')
		plot = convert_fig_to_html(fig)
		
		'''
	
			#pie chart
		'''
		count=[]
		labels=[]
		
		for i in np.arange(-2,10,2):
			t=[]
			val1=i
			val2=i+2
			query = "select count(*) from Earthquake where mag BETWEEN ' " + str(val1)+ " 'and ' " + str(val2)+ " ' " 
			con = sql.connect("database.db") 
			cur = con.cursor()
			cur.execute(query)
			rows = cur.fetchone()
			count.append(rows[0])
			t.append(val1)
			t.append(val2)
			labels.append(t)
			#print(t)
		#explode=(0.1,0,0.1,0,0.1,0)
		fig=plt.figure()
		colors=['y','g','r','b','c','b']
		explode = (0.1, 0, 0, 0,0,0)
		texts=plt.pie(count, colors=colors, explode=explode, labels=labels , autopct='%1.1f%%', shadow=True)
		plt.legend()
		#plt.show()
		plot=convert_fig_to_html(fig)
		'''
		#Histogram
		'''
		query="select mag from Earthquake"
		con = sql.connect("database.db") 
		cur = con.cursor()
		cur.execute(query)
		rows = cur.fetchall()
		y=pd.DataFrame(rows)
		x=y.dropna()
		num_bins=5
		fig=plt.figure()
		n,bins,patches=plt.hist(x[0] , bins=num_bins ,facecolor='blue' , alpha=0.5)
		#plt.show()
		plot=convert_fig_to_html(fig)
		'''
		#bar chart vertical
		
		count=[]
		labels_n=[]
		n = int(request.form["val1"])
		
		for i in np.arange(1000,30000,n):
			t=[]
			val1=i
			val2=i+n
			query = "select count(*) from Vote where  TotalPop BETWEEN ' " + str(val1)+ " 'and ' " + str(val2)+ " ' " 
			con = sql.connect("database.db") 
			cur = con.cursor()
			cur.execute(query)
			rows = cur.fetchone()
			count.append(rows[0])
			t.append(str(val1)+"-"+str(val2))
			#t.append(str(val2))
			labels_n.append(t)
			
		
		fig=plt.figure()
		y_pos =np.arange(len(labels_n))
		#print(y_pos)
		color=['r','b','g','y','c','b']
		for i  in range(len(count)):
			plt.bar(y_pos[i] , count[i] , color=color[i], align ='center',label="{0}".format(labels_n[i]))
			
		plt.xticks(y_pos,labels_n)
		plt.xlabel('count')
		plt.title('mag count')
		#plt.show()
		for i,v in enumerate(count):
			plt.text(i,v , str(v), color='r', fontweight='bold' , horizontalalignment='center') #vertical
			# plt.text(v,i , str(v), color='r', fontweight='bold') horizontal
			#print(v,i,str(v))
		
		plt.legend(numpoints=1)
		plot=convert_fig_to_html(fig)
		
		#barchart horizontal
		'''
		count=[]
		labels_n=[]
		
		for i in np.arange(-2,10,2):
			t=[]
			val1=i
			val2=i+2
			query = "select count(*) from Earthquake where mag BETWEEN ' " + str(val1)+ " 'and ' " + str(val2)+ " ' " 
			con = sql.connect("database.db") 
			cur = con.cursor()
			cur.execute(query)
			rows = cur.fetchone()
			count.append(rows[0])
			t.append(str(val1)+"-"+str(val2))
			#t.append(str(val2))
			labels_n.append(t)
			
		#print(labels_n)
		fig=plt.figure()
		y_pos =np.arange(len(labels_n))
		#print()
		color=['r','b','g','y','c','b']
		for i  in range(len(count)):
			plt.barh(y_pos[i] , count[i] , color=color[i], align ='center',label="{0}".format(labels_n[i]))
			
		plt.yticks(y_pos,labels_n)
		plt.xlabel('count')
		plt.title('mag count')
		#plt.show()
		for i,v in enumerate(count):
			#plt.text(i,v , str(v), color='r', fontweight='bold' , horizontalalignment='center') #vertical
			plt.text(v,i , str(v), color='r', fontweight='bold')
			#print(v,i,str(v))
		#legend = ['og_Male','og_Female','n_Male','n_Female']
		plt.legend(numpoints=1)
		plot=convert_fig_to_html(fig)
		'''
	return render_template("pie.html",data=plot.decode('utf8'))
	
@app.route('/linegraph')
def linegraph():
    query = "SELECT latitude,longitude FROM Earthquake "
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    y = pd.DataFrame(rows)
    X = y.dropna()
    fig = plt.figure()
    plt.plot(X[0], X[1],marker ='o',color='r',markeredgecolor='b')
    plt.title('Clusters based on latitude and longitude')
    plt.xlabel('latitude')
    plt.ylabel('longitude')
    plot = convert_fig_to_html(fig)
    return render_template("pie.html",data=plot.decode('utf8'))	
	
	

	


if __name__ == '__main__':
	app.run()