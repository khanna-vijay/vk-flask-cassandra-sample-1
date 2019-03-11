#    api.py
from flask import Blueprint, Response
from models.user import Person
from cassandra.cqlengine import connection
import util

from functools import wraps
import json
import flask

__author__ = "vijay"

api = Blueprint("api", __name__)

connection.setup(['127.0.0.1'], "cqlengine", protocol_version=3)

def json_api(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        result = f(*args, **kwargs)  # Call Function
        json_result = util.to_json(result)
        return Response(response=json_result,
                        status=200,
                        mimetype="application/json")

    return decorated_function


@api.route('/', defaults={"path": ""})
@api.route('/<path:path>')
def index(path=None):
    return "Hello World 2"


@api.route("/add", methods=["POST"])
@json_api
def add_person():
    data = json.loads(flask.request.data)
    #person = Person.create(first_name=data["first_name"], last_name=data["last_name"])
    person = Person.create(first_name="Vijay", last_name="Khanna")
    person.save()
    return person.get_data()


@api.route("/get-all")
@json_api
def get_all():
    persons = Person.objects().all()
    return [person.get_data() for person in persons]
