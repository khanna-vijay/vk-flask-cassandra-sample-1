# TestCass.py

from cassandra.cluster import Cluster
from flask import Flask, current_app, Blueprint

KEYSPACE = "cassandra_flask_vk"

from views.api import api

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)

    cluster = Cluster()
    session = cluster.connect()
    session.execute("DROP Keyspace IF EXISTS %s" % KEYSPACE)     # drop keyspace beforehand

    session.execute(
        """
        CREATE KEYSPACE IF NOT EXISTS %s WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
        """% KEYSPACE)
    session.set_keyspace("newflask")
    #session = clister.connect(keyspace="newflask")


    return app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081)
