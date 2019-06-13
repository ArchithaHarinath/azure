


port=int(os.getenv("VCAP_APP_PORT"))
app1.config['DB2_DATABASE'] = 'BLUDB'
app1.config['DB2_HOSTNAME'] =
"dashdb-txn-sbox-yp-dal09-03.services.dal.bluemix.net",
app1.config['DB2_PORT'] = 50000
app1.config['DB2_PROTOCOL'] = 'TCPIP'
app1.config['DB2_USER'] = 'ldp09495'
app1.config['DB2_PASSWORD'] = "d+hbtncwzz47kw92"


db=DB2(app1)

# @app1.route("/upload", methods=['POST'])
# def upload():
# file_name=request.form['file']
# sql="""LOAD DATA LOCAL INFILE %s INTO TABLE people FIELDS TERMINATED
BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1
LINES"""
# cursor=db.connection.cursor()
# #cursor.execute(sql,(file_name,))
# cursor.execute(sql)
# return render_template("main_page.html",message1="File Uploaded")
if __name__=="__main__":
app1.run(debug=True)




