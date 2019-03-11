# vk-flask-cassandra-sample-1
This code is used to setup a sample Read Write application

**On Application Server - Ubuntu 18 (AWS AMI) . Install Python, Pip, Flask ::
    sudo apt update

    sudo apt-get install python2.7
    sudo apt install python
    
#sudo apt install python3-pip
    
    sudo apt install python-pip
    pip --version
    sudo pip install --upgrade virtualenv 
    pip install Flask

**Test Sample Flask App . File Name : hello.py  runs on all IP's at port 8081 **

    from flask import Flask
    app = Flask(__name__)
    @app.route('/')
    def hello_world():
        return 'Hello World!'
    app.run(host="0.0.0.0", port=8081)

**Install Flask**
    #sudo apt install python3-flask
    sudo apt install python-flask
    export FLASK_APP=hello
    flask run
    
**Install Cassandra Driver**

    pip install cassandra-driver              //Takes some time..


**On Cassandra Server**

    sudo add-apt-repository ppa:webupd8team/java
    sudo apt-get update
    sudo apt-get install oracle-java8-set-default -y
    echo "deb http://www.apache.org/dist/cassandra/debian 36x main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list
    curl https://www.apache.org/dist/cassandra/KEYS | sudo apt-key add -
    sudo apt-get install cassandra
    nodetool status

    sudo apt install python-pip
    pip install cassandra-driver
    export CQLSH_NO_BUNDLED=true
    
    cqlsh
    DESC keyspaces
    SHOW VERSION
    
    CREATE KEYSPACE first_key_space WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 1};
    use first_key_space;
    CREATE TABLE emp_table_vk(
        emp_id int PRIMARY KEY,
        emp_name text,
        emp_city text,
        emp_sal varint,
        emp_phone varint
    );
    select * from emp_table_vk;
    ALTER TABLE emp_table_vk ADD emp_email text;
    BEGIN BATCH
    
    INSERT INTO emp_table_vk (emp_id, emp_city, emp_name, emp_phone, emp_sal) values(1 ,'Mumbai','Amit',1111999931, 44400);
    APPLY BATCH;
    
    select * from emp_table_vk ;
    
    //After Testing Standalone, point Cassandra to Physical localIP in the file  /etc/cassandra/cassandra.yaml
                rpc_address: 10.10.20.198
    service cassandra restart
    Test on Cassandra server.
                cqlsh 10.10.20.198
                
    

    
 **On Flask Server**
 ___________________
    
    git clone https://github.com/vijay-khanna/vk-flask-cassandra-sample-1.git
    mv vk-flask-cassandra-sample-1 flask-cassandra
    cd flask-cassandra/
    source venv/bin/activate
    pip install --upgrade pip
    ###venv> python -m pip uninstall pip
    
    pip install --upgrade cython
    
    pip install flask
    pip install cassandra-driver
    pip install flask_session
    

    export FLASK_APP=TestCass.py
    flask run

     sudo apt-get remove python3        //python3 creates issues sometimes here. 
     






    


