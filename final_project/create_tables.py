import pymysql#this is where the code breaks
from io import open
import pandas as pd
import networkx as nx
import json
import matplotlib.pyplot as plt 

# created database in mysql (before it stopped working) called "facebook"
# within this we created two tables "friend_attributes" and "friend_edges"
# error: "ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: NO)""
dbname="friends"
host="127.0.0.1"
user="root"
passwd=""
db=pymysql.connect(db=dbname, host=host, user=user,passwd=passwd, charset='utf8')

cur = db.cursor()

# turning the json files into lists
# so that we can iterate through them
# we made the number of attributes smaller because our  
# json data is not transferring and this is a simplified code we
# would have written, if we were able to test it.
def getFriendAttributes(attributes):
	attribute_data = []
	with open('friend_attributes') as f:
		for line in f:
			data.append(json.loads(line))#loads data from json
	return attribute_data #return this LIST of IDs
	# takes attribute_data from json and iterates it
	new_list = []
	for a in attribute_data:

		uid = a['uid']
		new_list.append(uid)

		name = a['name']
		new_list.append(name)

		birthday_date = a['birthday_date']
		new_list.append(birthday_date)

		sex = a['sex']
		new_list.append(sex)
	
	#take the newly created list and insert it into the attributes table
	fill_attributes_table= """INSERT INTO friend_attributes (uid, name, birthday_date, sex) VALUES (%s, %s, %s, %s);"""
	cur.execute(fill_attributes_table, new_list) # fill the table with appended list
	
	#list is created with all of the retrieved data
	return new_list

edge_list = []
def getFriendEdges(attributes):
	with open('friend_edges') as e:
		for line in e:
			data.append(json.loads(line))
		return edge_data

	for b in edge_data:
		edge_list = []

		uid = a['uid1']
		edge_list.append(uid1)

		name = a['uid2']
		edge_list.append(uid2)
	fill_edge_table= """INSERT INTO friend_edges (uid1, uid2) VALUES (%s, %s);"""
	cur.execute(fill_edge_table, edge_list) # fill the table with appended list
	
	return edge_list



db.commit()
cur.close()

# at this point MySQL is unaccessible so we cannot check if our code runs
# we would normally check it before moving forward, but we just moved on 
# assuming the code works
