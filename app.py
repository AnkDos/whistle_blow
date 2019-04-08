from flask import request
from flask import Flask, render_template , redirect , url_for

app = Flask(__name__)



@app.route('/')
def main():
    return  'Hello'  #render_template('hi.html')


if __name__ == '__main__' :
    app.run()