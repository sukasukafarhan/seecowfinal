''' controller and routes for label '''
import os
from flask import request, jsonify
from app import app, mongo
import logger
from app.schemas.label import validate_label
from app.services.response import response
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['csv'])

ROOT_PATH = os.environ.get('ROOT_PATH')
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(ROOT_PATH, 'output.log'))
    
def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/all_label', methods=['GET'])
def get_all_diseases():
  try:
    responses = response()
    label = mongo.db.labels
    output = []
    for s in label.find():
      output.append(
        {
          'namaLabel' : s['namaLabel'], 
          'labelIdentity': s['labelIdentity']
        })
    responses.setData(output)
    return jsonify(responses.getResponse())
  except :
    responses = response()
    responses.setStatus(False)
    responses.setMessage("Something wrong :(")
    return jsonify(responses.getResponse())


@app.route('/add_label', methods=['POST'])
def add_diseases():
  try:
    responses = response()
    data = validate_label(request.get_json())
    if data['ok']:
      data = data['data']
      mongo.db.labels.insert_one(data)
      responses.setMessage("Success add label on database")
      return jsonify(responses.getResponse())
    else:
      responses.setStatus(False)
      responses.setMessage("Something wrong :(")
      return jsonify(responses.getResponse())
  except:
    responses = response()
    responses.setStatus(False)
    responses.setMessage("Something wrong :(")
    return jsonify(responses.getResponse())

@app.route('/upload', methods=['POST'])
def upload_file():
  if 'file' not in request.files:
    return "no file"
  
  file = request.files['file']
  if file and allowed_file(file.filename):
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return "success"

# @app.route('/user', methods=['GET', 'POST', 'DELETE', 'PATCH'])
# def user():
#     if request.method == 'GET':
#         query = request.args
#         data = mongo.db.users.find({"username":"cobake5"})
#         return jsonify(data), 200

#     data = request.get_json()
#     if request.method == 'POST':
#         if data.get('name', None) is not None and data.get('email', None) is not None:
#             mongo.db.users.insert_one(data)
#             return jsonify({'ok': True, 'message': 'User created successfully!'}), 200
#         else:
#             return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400

#     if request.method == 'DELETE':
#         if data.get('email', None) is not None:
#             db_response = mongo.db.users.delete_one({'email': data['email']})
#             if db_response.deleted_count == 1:
#                 response = {'ok': True, 'message': 'record deleted'}
#             else:
#                 response = {'ok': True, 'message': 'no record found'}
#             return jsonify(response), 200
#         else:
#             return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400

#     if request.method == 'PATCH':
#         if data.get('query', {}) != {}:
#             mongo.db.users.update_one(
#                 data['query'], {'$set': data.get('payload', {})})
#             return jsonify({'ok': True, 'message': 'record updated'}), 200
#         else:
#             return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400
