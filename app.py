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

@app.route('/')
def getEvents():
	res = runQuery("SELECT * FROM event_type")
	# print(res)
	if res == []:
		return '<h4>No Movies Title</h4>'
	else:
		return render_template('events.html',events = res)


# @app.route('/')
# def renderLoginPage():
#     return render_template('./index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0') 
