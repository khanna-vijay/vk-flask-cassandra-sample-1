# vk-flask-cassandra-sample-1
This code is used to setup a sample Read Write application

1. On Application Server - Ubuntu 18 (AWS AMI) . Install Python, Pip, Flask
sudo apt update
sudo apt-get install python2.7
sudo apt install python

#sudo apt install python3-pip
sudo apt install python-pip
pip --version
sudo pip install --upgrade virtualenv 
pip install Flask


Test Sample Flask App

--hello.py...runs on all IP's at port 8081
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

app.run(host="0.0.0.0", port=8081)
--

#sudo apt install python3-flask
sudo apt install python-flask

export FLASK_APP=hello
flask run

pip install cassandra-driver              //Takes some time..


