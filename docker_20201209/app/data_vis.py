import pymysql
import pandas as pd


class data_vis():

    def __init__(self, sql):
        self.sql = sql
  
    def query(self):
        conn = pymysql.connect(host='172.17.0.2', port=3306, user='root', \
                       passwd='1234', charset='utf8')
        cursor = conn.cursor() 
        cursor.execute(self.sql)
        df = pd.DataFrame(list(cursor.fetchall()))		     
        print("df:",df.head(3))
        cursor.close()
        conn.close()