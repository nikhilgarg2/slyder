from .connect import *
import MySQLdb
import time
import re


def reconcile(category):
    sql="SELECT * FROM `item` WHERE `category_id`=%d" % int(category)
    cursor.execute(sql)
    fetch=cursor.fetchall()
    if len(fetch)==0:
        sql="SELECT `name` FROM `dump_val`"
        cursor.execute(sql)
        fetch=cursor.fetchall()
        for e in range(len(fetch)):
            x=str(fetch[e][0]).lower()
            x=re.sub(r'[^a-z^A-Z^0-9^\ ^\.^\%]','',x)
            sql2="INSERT INTO `item`(`name`,`category_id`) VALUES(%s,%s)"
            values=(x,category)
            cursor.execute(sql2,values)
            db.commit()
        sql="SELECT * FROM `dump_val`"
        cursor.execute(sql)
    else:
        do blah blah blah 