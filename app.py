from flask import request
from flask import Flask, render_template , redirect , url_for

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
    if action == 'blow_whistle' :
        return render_template('blow_whistle.html')
    elif action == 'share_opinion' :
        return render_template('share_opinion.html')    

@app.route('/emp/blow_whistle/subm' , methods = ['GET','POST'])
def submit_whist() :
    return "hi"     

@app.route('/emp/share_opinion/subm' , methods = ['GET' , 'POST'])
def submit_opp() :
    return "his"


if __name__ == '__main__' :
    app.run()