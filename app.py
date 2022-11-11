import mysql.connector,sys
import datetime
from mysql.connector import Error
from flask import Flask, request, jsonify, render_template,redirect, url_for
from random import randint


app = Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def renderLoginPage():
    events = runQuery("SELECT * FROM events")
    branch =  runQuery("SELECT * FROM branch")
    if request.method == 'POST':
        Tcount = runQuery("SELECT COUNT(*) FROM participants ")[0] 
        count = Tcount[0] + 1
        Name = request.form['FirstName'] + " " + request.form['LastName']
        Mobile = request.form['MobileNumber']
        Branch_id = request.form['Branch']
        Event = request.form['Event']
        Email = request.form['Email']
        # print(Name,Mobile,Branch,Event)
        runQuery("INSERT INTO participants VALUES({},{},\"{}\",\"{}\",\"{}\",\"COEP\",\"{}\");".format(count,Event,Name,Email,Mobile,Branch_id))
        return redirect('/')
    return render_template('index.html',events = events,branchs = branch)
    


@app.route('/loginfail')
def renderLoginFail():
    return render_template('loginfail.html')

@app.route('/admin', methods=['GET', 'POST'])
def renderAdmin():
    if request.method == 'POST':
        UN = request.form['username']
        PS = request.form['password']

        if UN=='Admin' and PS=='password':
            return redirect('/eventType')
        elif UN!='Admin':
            return render_template('admin.html',errors=["Wrong Username"])
        else:
            return render_template('admin.html',errors=["Wrong Password"])
    return render_template('admin.html')    

@app.route('/eventType',methods=['GET','POST'])
def getEvents():
    res = runQuery("SELECT *,(SELECT COUNT(*) FROM participants AS P WHERE P.event_id = E.type_id ) AS count FROM event_type AS E;")
    if request.method == "POST":
        Name = request.form["Newevent"]
        fee=request.form["Fee"]
        participants = request.form["MAXP"]
        imglink=request.form["LNK"]
        Type=request.form["typeid"]
        runQuery("INSERT INTO events(event_title,event_price,participents,img_link,type_id) VALUES(\"{}\",\"{}\",\"{}\",\"{}\",\"{}\");".format(Name,fee,participants,imglink,Type))
    if res == []:
        return '<h4>No Event Types</h4>'
    else:
        return render_template('events.html',events = res)
    

def runQuery(query):
    try:
        db = mysql.connector.connect(
            host='localhost',
            database='event_mgmt',
            user='root',
            password='password')

        if db.is_connected():
            print("Connected to MySQL, running query: ", query)
            cursor = db.cursor(buffered = True)
            cursor.execute(query)
            db.commit()
            res = None
            try:
                res = cursor.fetchall()
            except Exception as e:
                print("Query returned nothing, ", e)
                return []
            return res

    except Exception as e:
        print(e)
        return e

    db.close()

    print("Couldn't connect to MySQL")
    #Couldn't connect to MySQL
    return None


if __name__ == "__main__":
    app.run(host='0.0.0.0') 
