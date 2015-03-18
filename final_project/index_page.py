from flask import Flask, render_template, request, redirect, url_for
import pymysql
from io import open
import pandas as pd
import networkx as nx
import json
from create_tables2 import *
import matplotlib.pyplot as plt

dbname="friends"
host="127.0.0.1"
user="root"
passwd=" "
db=pymysql.connect(db=dbname, host=host, user=user,passwd=passwd, charset='utf8')

cur = db.cursor()

app=Flask(__name__)

@app.route('/') #base web address
# this function just renders index.html when
# someone goes to http://127.0.0.1:5000/
def make_index_resp():
    # we are taking the uid and names from the file friend_attributes
    # since we imported pymysql earlier, mysql commands should function
	cur.execute('''SELECT uid, name FROM friend_attributes ORDER BY name;''')
	friend_attributes = cur.fetchall()
	#this will return a list of Friends on the index page
    return(render_template('index.html', friend_attributes=friend_attributes)) 

@app.route('/profile/<uid>') #static route
def make_profiles_resp():
	# goes to database, finds friend and their selected 
	# attributes on their profile from the MySQL Table
	cur.execute('''SELECT * FROM friend_attributes''')
	# created a dictionary to put the tuple 
	d = {}
	for tup in cur.fetchall():
		print tup
		(uid, name, birthday_date, sex) = tup
		d[uid] = name
	#this displays the attributes on a friend's profile page
	return render_template('friends.html',uid=uid)

		# this has panda reading the data from friend_edges
		edgeList = pd.read_sql("SELECT * FROM friend_edges", db)
		# this next function takes a name
		# then returns a list of thier friends
		def friends_list(name):
			



if __name__ == '__main__': 
	app.run() 


