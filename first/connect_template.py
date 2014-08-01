
'''
create a file named connect.py in the first folder. The template is given below... Change user,password and database
details accordingly
'''

import MySQLdb

db=MySQLdb.connect("localhost","root","dellxps123","slyder")
cursor=db.cursor()

