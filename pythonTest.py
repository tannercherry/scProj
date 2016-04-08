#made by Tanner Cherry

import mysql.connector 

user1 = input('Please enter the username for your database: ')
password1 = input('Please enter the password for your database: ')
database = input('Please enter the name of your database: ')

db = mysql.connector.connect(host="localhost", user = user1, password = password1, db = database)
cursor = db.cursor()
hold, hold2, hold3 = 0, 0, 0
while hold == 0:
	user= input('Please enter your username: ')
	if user == user1:
		hold = 1
		while hold2 == 0:
			password = input('Please enter your password: ')
			if password == password1:
				hold2 = 1
				while hold3 == 0:
					lang = input('Which language do you need a developer for? Java, Python, HTML, C++, or Ruby?')
					if lang in ('Java', 'Python', 'HTML', 'C++', 'Ruby', 'java', 'python', 'html', 'c++', 'ruby'):
						myQuery = ("SELECT Name, Email FROM developer as d join skillsjoint as sj on d.ID = sj.DeveloperID join skills as s on sj.SkillID = s.ID where s.skill = '"+lang+"'")
						cursor.execute(myQuery)
						data = cursor.fetchall()
						print (data)
						hold3 = 1
					else:
						print('We do not have that language, please try again!')
			else:
				print('Wrong password, please try again!')

	else:
		print('Wrong username, please try again!')

cursor.close()