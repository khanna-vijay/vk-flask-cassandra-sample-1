from cassandra.cluster import Cluster
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from flask import Flask, session
from flask_session.__init__ import Session
from models.user import Person
from views.api import api



app = Flask(__name__)
sess = Session()

KEYSPACE = "cassandra_final_try"


def create_app():
    app = Flask(__name__)

    app.debug = True
    app.register_blueprint(api)

    cluster = Cluster()
    session = cluster.connect()
    session.execute(
        """
        CREATE KEYSPACE IF NOT EXISTS %s WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
        """ % KEYSPACE)
    session = cluster.connect(keyspace=KEYSPACE)

    return app


app = create_app()

if __name__ == '__main__':

    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    sess.init_app(app)

    connection.setup(['127.0.0.1'], "cqlengine", protocol_version=3)
    sync_table(Person)
    app.run(host="0.0.0.0", port=8081)
