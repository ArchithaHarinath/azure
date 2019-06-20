[2:04 PM, 6/20/2019] Architha: @app.route('/images',methods=['GET','POST'])
def images():
    list =[]
    result=[]
    if (request.method == 'POST'):
        lname = request.form['lname']
        cabin = request.form['cabin']

        query = "SELECT * FROM Earthquake where CabinNum = "+str(cabin) + " or Lname = '" + str(lname) + "'"
        #print(query)
        con = sql.connect("database.db")
        cur = con.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        return render_template("images.html",data=rows)
    return render_template('images.html')
[2:04 PM, 6/20/2019] Architha: <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>Shevi Jain 1344</h1>
<center>
    <form method="POST">
    Enter last name <input type="text" name="lname">
    Enter cabin name <input type="text" name="cabin">
    <input type="submit">
</form>
<table border="1">
    <tr>
        {% for row in data %}
        <td>
        {{ row[8] }}
            <img src="./static/{{ row[8] }}" height="70" width="70">
        {{ row[9] }}
            <img src="./static/{{ row[9] }}" height="70" width="70">
        </td>
        {% endfor %}
    </tr>

</table>

</center>
</body>
</html>

from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer

# Instantiate the clustering model and visualizer
model = KMeans()
visualizer = KElbowVisualizer(model, k=(4,12))

visualizer.fit(X)    # Fit the data to the visualizer
visualizer.poof() 