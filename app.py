import os.path
from flask import request
from flask import Flask, render_template , redirect , url_for , g
import sqlite3 as sql

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
    return "hi"     

@app.route('/emp/share_opinion/subm' , methods = ['GET' , 'POST'])
def submit_opp() :
    sub = request.form.get('sub')
    msg = request.form.get('msg')
    # return (sub + " " + msg)
    # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # db_path = os.path.join(BASE_DIR, "database.db")
    with sql.connect("dbz.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO opinion (sub,message) VALUES (?,?)",(sub,msg) )
        con.commit()    
        return redirect(url_for('action',action = 'share_opinion' ,msg = 'Thanks For Sharing With us , Will process soon !!!'))

        
#     con = sql.connect("database.db")
#     con.row_factory = sql.Row
#     cur = con.cursor()
#     cur.execute("select * from students") 
#     rows = cur.fetchall(); 








if __name__ == '__main__' :
    app.run()