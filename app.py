import os.path
import datetime
from flask import request
from flask import Flask, render_template , redirect , url_for , g
import sqlite3 as sql
import sys 
import os
sys.path.append(os.path.abspath("/home/ankur/whistle_blow/helpers"))
from sentinsar import *


app = Flask(__name__)



@app.route('/')
def main():
    return  render_template('landing.html')

@app.route('/<choice>')
def emp(choice) :
    if choice == 'emp' :
        return render_template('employee.html')
    elif choice == 'senr' :
        return render_template('seniors.html')
    else : 
        return "Wrong Choice Mate "

@app.route('/emp/<action>')
def action(action) :
    message = request.args.get('msg')
    if message is None :
        message = ''
    if action == 'blow_whistle' :
        return render_template('blow_whistle.html' ,message = message)
    elif action == 'share_opinion' :
        return render_template('share_opinion.html' ,message = message)    

@app.route('/emp/blow_whistle/subm' , methods = ['GET','POST'])
def submit_whist() :
    emp = request.form.get('emp')
    sub = request.form.get('sub')
    msg = request.form.get('msg')
    with sql.connect("dbs.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO whistles (emp_name,sub,message,sentiments,sarcasm) VALUES (?,?,?,?,?)",(emp,sub,msg,return_sentiments(msg),return_sarcasm(msg)))
        con.commit()    
    return redirect(url_for('action',action = 'share_opinion' ,msg = 'Thanks For Sharing With us , Will process soon !!!'))
    
    
@app.route('/emp/share_opinion/subm' , methods = ['GET' , 'POST'])
def submit_opp() :
    sub = request.form.get('sub')
    msg = request.form.get('msg')
    
    with sql.connect("dbs.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO opinion (sub,message,sentiments,sarcasm) VALUES (?,?,?,?)",(sub,msg,return_sentiments(msg),return_sarcasm(msg)))
        con.commit()    
        return redirect(url_for('action',action = 'share_opinion' ,msg = 'Thanks For Sharing With us , Will process soon !!!'))


@app.route('/senr/see_whistle')
def return_whistle():
    con = sql.connect("dbs.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from whistles")
    rows = cur.fetchall()
    return render_template('view_whistle.html' , rows = rows)
      
    

@app.route('/senr/see_opinions')
def return_opinions():
    con = sql.connect("dbs.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from opinion")
    rows = cur.fetchall()
    return render_template('view_opinion.html' , rows = rows)
    

@app.route('/update/add_whistle_remark')
def add_whistle_remarks() :
    reqs = request.args.get('post_id') 
    message = request.args.get('msg')
    if message is None :
        message = ''
    return render_template('update_whistle_remark.html' , post_id = reqs,message = message)

@app.route('/update/add_opinion_remark')
def add_opinion_remarks() :
    reqs = request.args.get('post_id')
    message = request.args.get('msg')
    if message is None :
        message = ''
    return render_template('update_opinion_remark.html' , post_id = reqs ,message = message)


@app.route('/senr/update_opinion' ,  methods = ['GET' , 'POST'])
def update_opinion() : 
    date_r = datetime.datetime.now()
    date_re = str(date_r).split('.')[0]
    pid    = request.form.get('pid')
    pid = int(pid)
    remark = request.form.get('remark')
    with sql.connect("dbs.db") as con:
        cur = con.cursor()
        cur.execute("update opinion set remark=?, date_re=? where sno=?", (remark, date_re, pid))
        con.commit()    
     
    return redirect(url_for('add_opinion_remarks',msg = 'updated_opinion'))


@app.route('/senr/update_whistle', methods = ['GET' , 'POST'])
def update_whistle() :
    
    date_r = datetime.datetime.now()
    date_re = str(date_r).split('.')[0]
    pid    = request.form.get('pid')
    pid = int(pid)
    remark = request.form.get('remark')
    with sql.connect("dbs.db") as con:
        cur = con.cursor()
        cur.execute("update whistles set remark=?, date_re=? where sno=?", (remark, date_re, pid))
        con.commit() 

    return redirect(url_for('add_whistle_remarks',msg = 'updated_whistle'))

if __name__ == '__main__' :
    app.run()