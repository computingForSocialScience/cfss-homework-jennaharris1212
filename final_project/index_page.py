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
def make_index_resp():
    # this function just renders index.html when
    # someone goes to http://127.0.0.1:5000/
    db=pymysql.connect(db=dbname, host=host, user=user,passwd=passwd, charset='utf8')
	c = db.cursor()
	c.execute('''SELECT uid, name FROM friend_attributes ORDER BY name;''')
	friend_attributes = c.fetchall()
	#this will return a list of Friend on the webpage
    return(render_template('index.html', friend_attributes=friend_attributes)) 

@app.route('/profile/<uid>') #static route
def make_profiles_resp():
	# goes to database, finds friend and their selected 
	# attributes on their profile from the MySQL Table
	cur.execute('''SELECT name, birthday_date, sex 
	FROM friends
	WHERE uid=%s;''')
	friend_attributes = cur.fetchall()
	#this displays the attributes on a friend's profile page
	return render_template('friends.html',uid=uid)


if __name__ == '__main__': 
	app.run() 
