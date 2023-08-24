from flask import request , jsonify,g
import requests
import json
from flask import Flask, render_template
from db import init_db,get_db,close_db,find_id_user

app = Flask(__name__)


@app.before_request # 요청이 오기 직전에 db 연결
def before_request():
    get_db()

@app.teardown_request # 요청이 끝난 직후에 db 연결 해제
def teardown_request(exception):
    close_db()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/find_team' , methods=['GET', 'POST'])
def find_team():
    if request.method=='GET':
        return render_template('index.html')
    else:
        team=request.form['team_name']
        result=find_id_user(g.db,team)
        print(result)
        return render_template('show_table.html',data_list=result)


if __name__ =="__main__" :
    init_db()
    app.run(host='0.0.0.0', port=5000)
