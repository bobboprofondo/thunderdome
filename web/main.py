# Python 3 server to manage Light The Thunderdome
from flask import Flask, render_template, request
app = Flask("/web/main")
import time


hostName = "ledpi.local"
#hostName = "0.0.0.0"
serverPort = 8080

#App variables for test
RGBVal = {
    0: 0, 
    1: 0, 
    2: 0
    }

@app.route("/")
def main():
    templateData = {
        'rgb' : RGBVal
    }
    return render_template('web/main.html', **templateData)

if __name__ == "__main__":        
    app.run(host=hostName, port=serverPort, debug=True)