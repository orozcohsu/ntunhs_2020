from flask import Flask, request, render_template, make_response
import os
from data_vis import data_vis

app = Flask(__name__)

@app.route('/')
def main_form():
    return render_template('main_form.html')

@app.route('/', methods=['POST'])
def main_form_post():
    sql = request.form['sql']
    if os.path.isfile('/app/static/out.png'):
        os.remove('/app/static/out.png')
    obj = data_vis(sql)
    obj.query()
	
    return make_response('',204)

@app.route("/get_img")
def get_img():
    return "out.png"
	
@app.route("/get_ready_img")
def get_ready_img():
    if os.path.isfile('/app/static/out.png'):
        return make_response('false',200)
    else:
        return make_response('true',200)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

