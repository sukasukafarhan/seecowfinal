
''' flask app with mongo '''
import os
import json
import datetime
from bson.objectid import ObjectId
from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

class JSONEncoder(json.JSONEncoder):
    ''' extend json-encoder class'''

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)


# create the flask object
UPLOAD_FOLDER = './static/'

app = Flask(__name__)

# add mongo url to flask config, so that flask_pymongo can use it to make connection
app.config['MONGO_URI'] = os.environ.get('DB')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JWT_SECRET_KEY'] = os.environ.get('SECRET')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
# app.config['MONGO_DBNAME'] = 'seecow_db'
# app.config['MONGO_URI'] = 'mongodb://mongo:27017/seecow_db'
mongo = PyMongo(app)

# use the modified encoder class to handle ObjectId & datetime object while jsonifying the response.
app.json_encoder = JSONEncoder

from app.controllers import *