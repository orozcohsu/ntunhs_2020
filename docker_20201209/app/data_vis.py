import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class data_vis():

    def __init__(self, sql):
        self.sql = sql
  
    def query(self):
        try:
            conn = pymysql.connect(host='172.17.0.2', port=3306, user='root', \
                                   passwd='1234', charset='utf8')
            cursor = conn.cursor() 
            cursor.execute(self.sql)

            df = pd.DataFrame(list(cursor.fetchall()))	
            df = df.rename(columns={0: "emp_no", 1: "age", 2: "salary", 3: "gender"})			
        
            sns.set_context("talk", font_scale=1.1)
            plt.figure(figsize=(10,6))
            sns.scatterplot(x="age", y="salary", sizes=(20,500), alpha=0.5, \
		                    hue="gender", data=df)

            plt.legend(bbox_to_anchor=(1.01, 1),borderaxespad=0)
            plt.xlabel("Age")
            plt.ylabel("Salary")
            plt.title("Employee Salary")
            plt.tight_layout()
 
            plt.savefig("/app/static/out.png", format='png',dpi=80)
        except Exception as ex:
            print(ex)
        finally:
            cursor.close()
            conn.close()