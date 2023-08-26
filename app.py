from flask import request , jsonify,g
import requests
import json
from flask import Flask, render_template,render_template_string
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


@app.route('/find_team' , methods=['GET'])
def find_team():
    team=request.args.get('team','')
    result=find_id_user(g.db,team)
    print(result)
    template = '''
     <html>
        <head>
            <meta charset="UTF-8">
            <title>인사정보체계</title>
        </head>
        <body>
            <h1>%s에 대한 검색 결과</h1>
            <table border="1" id="table">
                <thead>
                    <tr>
                        <th width="200px">팀명</th>
                        <th width="250px">이름</th>
                    </tr>
                </thead>
                <tbody>
                    %s
                </tbody>
            </table>

            <a href="/">원래페이지</a>
        </body>
    </html>
    ''' % (team, ''.join('<tr><td width="200px">%s</td><td width="200px">%s</td></tr>' % (obj['team'], obj['name']) for obj in result))


    return render_template_string(template, data_list=result)


if __name__ =="__main__" :
    init_db()
    app.run(host='0.0.0.0', port=5000)
