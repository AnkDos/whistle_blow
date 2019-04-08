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




if __name__ == '__main__' :
    app.run()