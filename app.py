import mysql.connector,sys
import datetime
from mysql.connector import Error
from flask import Flask, request, jsonify, render_template
from random import randint


app = Flask(__name__)



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

# runQuery("INSERT INTO events VALUES(10,'OpenSource', 50,1,'cs04.jpg',1);")
# runQuery("DELETE FROM events WHERE event_title = 'OpenSource';")

@app.route('/')
def renderLoginPage():
    return render_template('./index.html')




if __name__ == "__main__":
    app.run(host='0.0.0.0') 
