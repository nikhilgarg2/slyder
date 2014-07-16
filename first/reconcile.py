from .connect import *
import MySQLdb
import time
import re
import fuzzywuzzy
from fuzzywuzzy import fuzz


def reconcile(category):
    sql="SELECT * FROM `item` WHERE `category_id`=%s"
    tal=category
    cursor.execute(sql,tal)
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
        fetch=cursor.fetchall()
        for e in range(len(fetch)):
            x=str(fetch[e][2]).lower()
            x=re.sub(r'[^a-z^A-Z^0-9^\ ^\.^\%]','',x)
            sql2="SELECT `id` FROM `item` WHERE `name`=%s"
            value=(x)
            cursor.execute(sql2,value)
            id1=cursor.fetchone()
            m= re.sub(r'[^0-9^\.]','',fetch[e][3])
            s= re.sub(r'[^0-9^\.]','',fetch[e][4])
            m= float(re.sub(r'^[^0-9]','',m))
            s= float(re.sub(r'^[^0-9]','',s))
            sql="INSERT INTO `item_done`(`crawl_id`,`item_id`,`cat_id`,`website_item`,`name`,`mrp`,`site_price`)\
                VALUES(%s,%s,%s,%s,%s,%s,%s)"
            values=(fetch[e][5],id1[0],category,fetch[e][1],x,m,s)
            cursor.execute(sql,values)
            db.commit()
        sql3="DELETE FROM `dump_val`"
        cursor.execute(sql3)
        db.commit()
        
    
    else:
        sql="SELECT * FROM `item_done` WHERE `cat_id`=%d" % int(category)
        
        cursor.execute(sql)
        array=cursor.fetchall()
        sql2="SELECT * FROM `dump_val`"
        cursor.execute(sql2)
        array2=cursor.fetchall()
        print 'true'
        for e in range(len(array2)):
            #print len(array2)
            x=str(array2[e][2]).lower()
            x= x=re.sub(r'[^a-z^A-Z^0-9^\ ^\.^\%]','',x)
            m= re.sub(r'[^0-9^\.]','',array2[e][3])
            s= re.sub(r'[^0-9^\.]','',array2[e][4])
            m= float(re.sub(r'^[^0-9]','',m))
            s= float(re.sub(r'^[^0-9]','',s))
            mrt=0
            t=False
            for j in range(len(array)):
                y=str(array[j][5])
                if 0.9*m <= float(array[j][6]) <= 1.1* m:    
                    rat=fuzz.token_set_ratio(x,y)
                    if rat>= 85 and rat > mrt:
                        t=True
                        mrt=rat    
                        i_id=array[j][2]    
           # print t
            if t==False:
                sql2="INSERT INTO `item`(`name`,`category_id`) VALUES(%s,%s)"
                values=(x,category)
                cursor.execute(sql2,values)
                db.commit()
                sql2="SELECT `id` FROM `item` WHERE `name`=%s"
                value=(x)
                cursor.execute(sql2,value)
                id1=cursor.fetchone()
                sql="INSERT INTO `item_done`(`crawl_id`,`item_id`,`cat_id`,`website_item`,`name`,`mrp`,`site_price`)\
                VALUES(%s,%s,%s,%s,%s,%s,%s)"
                values=(array2[e][5],id1[0],category,array2[e][1],x,m,s)
                cursor.execute(sql,values)
                db.commit()
           
           
            else:
                sql="INSERT INTO `item_done`(`crawl_id`,`item_id`,`cat_id`,`website_item`,`name`,`mrp`,`site_price`)\
                VALUES(%s,%s,%s,%s,%s,%s,%s)"
                values=(array2[e][5],i_id,category,array2[e][1],x,m,s)
                cursor.execute(sql,values)
                db.commit()
            
        sql3="DELETE FROM `dump_val`"
        cursor.execute(sql3)
        db.commit()