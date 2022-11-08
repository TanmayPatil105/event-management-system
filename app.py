import mysql.connector,sys
import datetime
from mysql.connector import Error
from flask import Flask, request, jsonify, render_template
from random import randint


app = Flask(__name__)


@app.route('/')
def renderLoginPage():
    res = runQuery("SELECT * FROM event_type")
    # count=runQuery("select count(*) from participants where participants.event_id = res[0][];")
    if res == []:
        return '<h4>No Event Types</h4>'
    else:
         return render_template('index.html',events = res)

@app.route('/loginfail')
def renderLoginFail():
    return render_template('loginfail.html')

@app.route('/admin')
def renderAdmin():
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
