import MySQLdb

db=MySQLdb.connect("localhost","root","dellxps123","dtry", use_unicode=1,charset="utf8")
cursor=db.cursor()