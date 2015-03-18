from flask import Flask, render_template, request, redirect, url_for
from io import open
import pymysql
import pandas as pd
import networkx as nx
import json
import matplotlib.pyplot as plt 
import tempfile
import warnings

dbname="facebook"
host="127.0.0.2"
user="root"
passwd=" "

db=pymysql.connect(db=dbname, host=host, user=user,passwd=passwd, charset='utf8')
c = db.cursor()

def get_edge_data(edges):
	uid = []
	# opens json file, loads it, and closes the file
	json_data = open(edges)
	friend_edges = json.load(json_data)
	json_data.close()

	# creates a list of tuples of names
	for i in friend_edges:
		uid.append((i['uid1'],i['uid2']))
	return uid

# takes file friend_attributes.json and returns a list of lists of info
def get_friend_info(attributes):
	friend_info = []

	# opens json file, loads it, and closes the file
	friend_attributes = open(attributes)
	friend_info_data = json.load(friend_attributes)
	friend_attributes.close()

	info_list = []

	# loops through loaded json data and creates a list of lists of information
	for i in friend_info_data:
		temp_info = []

		# getting uid
		uid = i['uid']
		temp_info.append(uid)

		# getting name
		name = i['name']
		temp_info.append(name.replace("'","''"))

		# getting pic
		pic = i['pic']
		temp_info.append(pic)

		# getting religion, if empty list fills in with none
		religion = i['religion']
		religion = i['religion']
		if religion == None or not religion:
			temp = None
		else:
			temp = []
			for each in religion:
				temp.append(each['type']+': '+each['name'])
			temp = ' | '.join(temp)
		temp_info.append(temp)

		#getting birthday if empty list fills in with none
		birthday_date = i['birthday_date']
		temp_info.append(birthday_date)

		# getting sex
		sex = i['sex']
		temp_info.append(sex)

		# getting home town if empty fills in with none
		hometown_location = i['hometown_location']
		if hometown_location != None:
			home_string = hometown_location['name']+', '+hometown_locationt['country']
		else:
			home_string = None
		temp_info.append(home_string)

		# getting current location, if empty fills in with none
		current_location = i['current_location']
		if current_location != None:
			current_location_string = current_location['name']+', '+current_location['country']
		else:
			current_location_string = None
		temp_info.append(current_location_string)

		# getting relationship_status, if empty fills in with none
		relationship_status = i['relationship_status']
		if relationship_status == "":
			relationship_status = None
		temp_info.append(relationship_status)

		# getting significant other
		significant_other_id = i['significant_other_id']
		temp_info.append(significant_other_id)

		# getting political
		political = i['political']
		temp_info.append(political)

		# getting locale
		locale = i['locale']
		temp_info.append(locale)

		# getting profile_url
		profile_url = i['profile_url']
		temp_info.append(profile_url)

		#getting website
		website = i['website']
		temp_info.append(website)

		#getting contact email if empty fills with none
		contact_email = i['contact_email']
		if contact_email == "":
			contact_email = None
		temp_info.append(contact_email)
		
		info_list.append(temp_info)
	return info_list

# takes a json file and creates a SQL table and inserts data
def create_edge_table(edges):
	#catches warnings and only inserts items if table isn't made
	with warnings.catch_warnings():
		warnings.filterwarnings('error')
		try:
			# creates SQL table
			sql_friend_edges = '''CREATE TABLE IF NOT EXISTS 
				friend_edges(uid1 varchar (100), uid2 varchar (100));'''
			c.execute(sql_friend_edges)
		except Warning:
			pass
		else:
			# Gets data in the form of a list of tuples
			uid = get_edge_data(edges)

			# Inserts data into SQL table
			insertQuery = '''INSERT INTO friend_edges(uid1, uid2) VALUES (%s, %s);'''
			c.executemany(insertQuery,uid)

# takes a json file and cretes a SQL table and inserts data
def create_attributes_table(attributes):
	# catches warnings and only inserts items if table isn't made
	with warnings.catch_warnings():
		warnings.filterwarnings('error')
		try:
			# creates SQL table
			sql_friend_attributes = '''CREATE TABLE IF NOT EXISTS friend_info
				(uid varchar (100), name varchar (100), pic varchar (100), religion varchar (100),
				birthday_date varchar (100), sex varchar(100), hometown_location varchar (100),
				current_location varchar(100), relationship_status varchar(100),
				significant_other_id varchar (100), political varchar (100),
				locale varchar(100), profile_url varchar(100), website varchar(256), contact_email varchar(100))'''		
					
			c.execute(sql_friend_attributes)
		except Warning:
			pass
		else:
			# gets info from json file
			friend_attributes = get_friend_info(attributes)

			# inserts data into SQL table
			insertQuery = '''INSERT INTO friend_info(uid, name, pic, religion,
				birthday_date, sex, hometown_location, current_location, relationship_status,
				significant_other_id, political, locale, profile_url, webstie, contact_email)
				VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''
			c.executemany(insertQuery, friend_attributes)

# creates and fills tables as long as these files exist
create_attributes_table("friend_attributes.json")
create_edge_table("friend_edges.json")

db.commit()
