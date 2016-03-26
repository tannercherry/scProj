#made by Tanner Cherry

import mysql.connector 

db = mysql.connector.connect(host="localhost", user="root", password="tfocherry", db="socialcoasterdb")
cursor = db.cursor()
hold, hold2, hold3 = 0, 0, 0
while hold == 0:
	user= input('Please enter your username: ')
	if user == 'root':
		hold = 1
		while hold2 == 0:
			password = input('Please enter your password: ')
			if password == 'tfocherry':
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