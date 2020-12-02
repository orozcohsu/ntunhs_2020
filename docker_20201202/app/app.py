from flask import Flask,  request, render_template
import pymysql

app = Flask(__name__)


def db():
    db = pymysql.connect(host='172.17.0.2', user='root', passwd='1234', db='ntuhs')

    cursor = db.cursor()
  
    sql="select first_name, last_name, gender, dept_name, max(salary) as salary, title from \
        (\
           select first_name, last_name, gender, dept_name, salary, title \
           from ntuhs.employees a \
           join ntuhs.dept_emp b \
           join ntuhs.departments c \
           join ntuhs.salaries d \
           join ntuhs.titles e \
           on a.emp_no = b.emp_no and b.dept_no = c.dept_no and a.emp_no = d.emp_no \
           and a.emp_no = e.emp_no \
       ) f \
       group by first_name, last_name, gender, dept_name, title"

    cursor.execute(sql)

    rows = cursor.fetchall()

    db.close()

    return rows
    

rows = db()

for row in rows:
    print(row[0] + " - " + row[1] + " - " + row[2] + " - " + row[3] + " - " + str(row[4]) + " - " + row[5])

@app.route('/', methods=['GET'])
def emp():
    rows = db()
    return render_template ('index.html', employees = rows)
	
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
