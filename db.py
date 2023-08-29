from flask import g,Blueprint
from contextlib import nullcontext
from pymysql import cursors, connect
import pymysql
import pandas as pd
def init_db():

    db = connect(host='127.0.0.1', user='root', password='root', db='senahr', charset='utf8',cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()   #커서
   
    with db.cursor() as cursor: #DB가 없으면 만들어라.
        sql = "CREATE DATABASE IF NOT EXISTS senahr "
        cursor.execute(sql)
    db.commit()

    db.select_db('senahr')
    
    with db.cursor() as cursor: #DB가 없으면 만들어라.
    
        sql1= "CREATE TABLE IF NOT EXISTS senahr.`user` (`user_id` VARCHAR(100) NOT NULL, `name` VARCHAR(100) NOT NULL,`security_number` VARCHAR(100) , `phone_number` VARCHAR(100) ,`address` VARCHAR(100),`team` VARCHAR(100),`account` VARCHAR(100))"
        cursor.execute(sql1) 

    db.commit
    db.close

def get_db(): #이거 개중요
    if 'db' not in g:     # 플라스크의 전역변수 g 속에 db 가 없으면
        g.db = connect(host='127.0.0.1', user='root', password='root', db='senahr', charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)
        # 내꺼 db에 접속.

def close_db(): #db 연결 종료
    db=g.pop('db',None) #db라는 거를 팝.
    if db is not None: #팝 한게 비어있지 않으면
        if db.open: #db가 열려있으면
            db.close() #종료해라


def find_id_user(db, team):
    with db.cursor() as cursor:
        sql= "select * from senahr.user where team=%s"
        cursor.execute(sql, team)
        result = cursor.fetchall()
        #db에 id가 존재함
        return result     
    
def find_user(db):
    with db.cursor() as cursor:
        sql= "select * from senahr.user"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result     