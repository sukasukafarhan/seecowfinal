''' controller and routes for label '''
import os
from flask import request, jsonify
from app import app, mongo
import logger
from app.schemas.label import validate_label
from app.services.response import response
from werkzeug.utils import secure_filename
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO   
from sklearn.tree import _tree 
import pydotplus
import pickle

ALLOWED_EXTENSIONS = set(['csv'])

ROOT_PATH = os.environ.get('ROOT_PATH')
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(ROOT_PATH, 'output.log'))
    
# =======SECTION LABEL=======
@app.route('/label/all_label', methods=['GET'])
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


# @app.route('/label/add_label', methods=['POST'])
# def add_diseases():
#   try:
#     responses = response()
#     data = validate_label(request.get_json())
#     if data['ok']:
#       data = data['data']
#       mongo.db.labels.insert_one(data)
#       responses.setMessage("Success add label on database")
#       return jsonify(responses.getResponse())
#     else:
#       responses.setStatus(False)
#       responses.setMessage("Something wrong :(")
#       return jsonify(responses.getResponse())
#   except:
#     responses = response()
#     responses.setStatus(False)
#     responses.setMessage("Something wrong :(")
#     return jsonify(responses.getResponse())

def getLabel():
  try:
    label = mongo.db.labels
    output = []
    for s in label.find():
      output.append(s['namaLabel'])
    return output
  except :
    return False

# =======SECTION DECISION TREE=======
def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_header(data):
  # GET HEADER
  colls_name = []
  for i in data:
    colls_name.append(data[i][0])

  return colls_name

def get_features(colls_name):
  # GET ATTRIBUTE / FEATURES
  feature_cols = colls_name[0:len(colls_name)-1]
  iteration = 0
  mongo.db.attributes.drop()
  for i in range(len(feature_cols)):
    data = {
      "namaAttribute" : feature_cols[i],
      "attributeIdentitiy" : iteration
    }
    iteration+=1
    mongo.db.attributes.insert_one(data)

  return feature_cols

def save_labels(data):
  labels_unique = data.Label.unique()
  iteration=0
  mongo.db.labels.drop()
  for i in range(len(labels_unique)):
    data = {
      "namaLabel" : labels_unique[i],
      "labelIdentity" : iteration
    }
    iteration+=1
    mongo.db.labels.insert_one(data)
  data['Label'] = pd.factorize(data.Label)[0]
  return data

def pre_processing(data,colls_name):
  # PREPROCESSING DATA
  # - drop header by index
  # - convert to array to normalize index after dropping
  # - convert to dataframe and add coloumns name
  data_after_drop_label = data.drop([0])
  data_array = data_after_drop_label.values
  data_training = pd.DataFrame(data=data_array)
  data_training.columns = colls_name
  data_ready = save_labels(data_training)
  return data_ready

def training(data_training,feature_cols):
  X = data_training[feature_cols]
  y = data_training.Label
  clf = DecisionTreeClassifier()
  clf = clf.fit(X,y)
  return clf

def save_model(model):
  # SAVING TO PICKLE
  pkl_filename = "pickle_model.pkl"
  with open(pkl_filename, 'wb') as file:
    pickle.dump(model, file)


@app.route('/intelligent/upload_training_data', methods=['POST'])
def upload_file():
  try:
   file = request.files['file']
   if file and allowed_file(file.filename):
     filename = secure_filename(file.filename)
     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
     data = pd.read_csv("././static/data-coba-coba.csv",header=None)
     # GET HEADER
     colls_name = get_header(data)
     # GET ATTRIBUTE
     feature_cols = get_features(colls_name)
     # PRE PROCESSING
     data_training = pre_processing(data,colls_name)
     # TRAINING
     model = training(data_training,feature_cols)
     # SAVE MODEL
     save_model(model)
     responses = response()
     responses.setStatus(True)
     responses.setMessage("Succesfully save model")
     return jsonify(responses.getResponse())

  except:
    responses = response()
    responses.setStatus(False)
    responses.setMessage("Something wrong :(")
    return jsonify(responses.getResponse())

# @app.route('/intelligent/testing_data', methods=['POST'])
# def testing_data():
#   try:
    
  
#   except:

#   if 'file' not in request.files:
#     return "no file"

#   file = request.files['file']
#   if file and allowed_file(file.filename):
#     filename = secure_filename(file.filename)
#     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#     col_names = ['Ambing dan puting bengkak', 'Susus berubah warna', 'Sapi kesakitan bila ambing dipegang', 'Ambing keras dan panas bila dipegang',
# 'Sisi perut sebelah kiri membesar','Lambung bila dipukul berbunyi seperti drum','Tidak nafsu makan','Gelisah','Air ludah banyak berbuih dan ngiler',
# 'Adanya lepuh lepuh pada gusi,lidah,sekitar kuku dan di ambing susu','Suhu tubuh tinggi','Bengkak di daerah leher,dada,sisi lambung,pinggang dan alat kelamin luar',
# 'Pendarahan pada dubur,mulut,hidung, dan urin bercampur darah','Menanduk benda di sekitarnya','Keguguran pada umur kebuntingan 5-8 bulan','Keluar cairan keruh saat keguguran',
# 'Produksi susu menurun','Kulit di bawah mata kuning','Abortus atau keguguran terjadi selama1-3 minggu','Urin berwarna merah gelap hampir hitam','Kejang kejang',
# 'Terdapat luka di sapi','Menggaruk atau menggesek tubuhnya','Ada kerak atau kopeng pada permukaan kulit','Bulu rontok','label']
#     pima = pd.read_csv("././static/data_dari_koleksi_2.csv", header=None, names=col_names)
#     return str(pima['label'])
