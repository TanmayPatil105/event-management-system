import mysql.connector,sys
import datetime
from mysql.connector import Error
from flask import Flask, request, jsonify, render_template,redirect, url_for
from random import randint


app = Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def renderLoginPage():
    res = runQuery("SELECT * FROM event_type")
    if request.method == 'POST':
        Tcount = runQuery("SELECT COUNT(*) FROM participants ")[0] 
        count = Tcount[0] + 1
        Name = request.form['FirstName'] + " " + request.form['LastName']
        Mobile = request.form['MobileNumber']
        Branch = request.form['Branch']
        Event = request.form['Event']
        # print(Name,Mobile,Branch,Event)
        runQuery("INSERT INTO participants VALUES({},{},\"{}\",\"xyz@gmail.com\",\"{}\",\"COEP\",\"{}\");".format(count,Event,Name,Mobile,Branch))
        return redirect('/')
    return render_template('index.html',events = res)
    


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
        else:
            return render_template('admin.html')
    return render_template('admin.html')    

@app.route('/eventType')
def getEvents():
    res = runQuery("SELECT *,(SELECT COUNT(*) FROM participants AS P WHERE P.event_id = E.type_id ) AS count FROM event_type AS E;")
    # print(res)
    if res == []:
        return '<h4>No Event Types</h4>'
    else:
        return render_template('events.html',events = res)

def runQuery(query):
    try:
        db = mysql.connector.connect(
            host='localhost',
            database='event',
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
