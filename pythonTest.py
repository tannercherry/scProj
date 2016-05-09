#made by Tanner Cherry

import mysql.connector 

user1 = input('Please enter the username for your database: ')
password1 = input('Please enter the password for your database: ')
database = input('Please enter the name of your database: ')

db = mysql.connector.connect(host="localhost", user = user1, password = password1, db = database)
cursor = db.cursor()
hold = 0

while test == 0:
	task = input('Would you like to add data or look at data? Please enter "add" or "look"')
	if task in ('add'):
		test = 0;
		myQuery = (
		cursor.execute(myQuery)
		

	if task in ('look'):
		test = 0;
		while hold == 0:
			lang = input('Which language do you need a developer for? Java, Python, HTML, C++, or Ruby?')
			if lang in ('Java', 'Python', 'HTML', 'C++', 'Ruby', 'java', 'python', 'html', 'c++', 'ruby'):
				myQuery2 = ("SELECT Name, Email FROM developer as d join skillsjoint as sj on d.ID = sj.DeveloperID join skills as s on sj.SkillID = s.ID where s.skill = '"+lang+"'")
				cursor.execute(myQuery2)
				data = cursor.fetchall()
				print (data)
				hold = 1
			else:
				print('We do not have that language, please try again!')

cursor.close()