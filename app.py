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
        Name = request.form['FirstName'] + " " + request.form['LastName']
        Mobile = request.form['MobileNumber']
        Branch_id = request.form['Branch']
        Event = request.form['Event']
        Email = request.form['Email']

        if len(Mobile) != 10:
            return render_template('index.html',events = events,branchs = branch, errors = ["Invalid Mobile Number!"])

        if Email[-4:] != '.com':
            return render_template('index.html',events = events,branchs = branch, errors = ["Invalid Email!"])

        if len(runQuery("SELECT * FROM participants WHERE event_id={} AND mobile={}".format(Event,Mobile))) > 0 :
            return render_template('index.html',events = events,branchs = branch, errors = ["Student already Registered for the Event!"])

        if runQuery("SELECT COUNT(*) FROM participants WHERE event_id={}".format(Event)) >= runQuery("SELECT participants FROM events WHERE event_id={}".format(Event)):
            return render_template('index.html',events = events,branchs = branch, errors = ["Participants count fullfilled Already!"])

        runQuery("INSERT INTO participants(event_id,fullname,email,mobile,college,branch_id) VALUES({},\"{}\",\"{}\",\"{}\",\"COEP\",\"{}\");".format(Event,Name,Email,Mobile,Branch_id))

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

        cred = runQuery("SELECT * FROM admin")

        print(cred)

        if UN==cred[0][0] and PS==cred[0][1]:
            return redirect('/eventType')
        elif UN!='Admin':
            return render_template('admin.html',errors=["Wrong Username"])
        else:
            return render_template('admin.html',errors=["Wrong Password"])
    return render_template('admin.html')    



@app.route('/eventType',methods=['GET','POST'])
def getEvents():
    res = runQuery("SELECT *,(SELECT COUNT(*) FROM participants AS P WHERE P.event_id = E.type_id ) AS count FROM event_type AS E;") # Query to be modified
    types = runQuery("SELECT * FROM event_type;")
    location = runQuery("SELECT * FROM location")
    if request.method == "POST":
        Name = request.form["newEvent"]
        fee=request.form["Fee"]
        participants = request.form["maxP"]
        Type=request.form["EventType"]
        Location = request.form["EventLocation"]
        runQuery("INSERT INTO events(event_title,event_price,participants,type_id,location_id) VALUES(\"{}\",{},{},{},{});".format(Name,fee,participants,Type, Location))
    return render_template('events.html',events = res,types = types,locations = location)

@app.route('/eventinfo')
def rendereventinfo():
    events=runQuery("select * from events left join event_type using(type_id) left join location using(location_id);")
    if events == []:
        return '<h2>Sorry, We have no upcoming events &#128546;<h2>'
    else:
        return render_template('events_info.html',events = events)
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
