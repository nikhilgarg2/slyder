from selenium import webdriver
import MySQLdb
import time
#from .compile import compile1
from .connect import *

def dump2(crawl):
    sql="SELECT * FROM `item_done` WHERE `crawl_id`=%s"
    values=(crawl)
    cursor.execute(sql,values)
    final=cursor.fetchall()
    
    for e in range(len(final)):
        x=final[e]
        sql="INSERT INTO `item_done_fin`(`crawl_id`,`item_id`,`cat_id`,`website_item`,`name`,`mrp`,`site_price`)\
                VALUES(%s,%s,%s,%s,%s,%s,%s)"
        values=(x[1],x[2],x[3],x[4],x[5],x[6],x[7])
        cursor.execute(sql,values)
        db.commit()
    
    sql1="DELETE FROM `item_done` WHERE `crawl_id`=%s"
    val=(crawl)
    cursor.execute(sql1,val)
    db.commit()