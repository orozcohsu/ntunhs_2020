from flask import Flask, request, render_template, make_response
import os, glob
from data_vis import data_vis

app = Flask(__name__)

@app.route('/')
def main_form():
    #delete image file
    files = glob.glob('/app/static/*')
    for f in files:
        os.remove(f)
		
    return render_template('main_form.html')

@app.route('/', methods=['POST'])
def main_form_post():
    #get sql string from web
    sql = request.form['sql']

    #delete image file
    files = glob.glob('/app/static/*')
    for f in files:
        os.remove(f)    

    #start to query data and visualize
    obj = data_vis(sql)
    obj.query_vis()
	
    return make_response('',204)

@app.route("/get_img")
def get_img():
    import glob
    files = glob.glob('/app/static/*')
    for f in files:
        return os.path.basename(f)
	
@app.route("/get_ready_img")
def get_ready_img():
    import glob
    files = glob.glob('/app/static/*')
    for f in files:
        if os.path.isfile(str(f)):
            return make_response('false',200)
    else:
        return make_response('true',200)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

