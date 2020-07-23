# author : faruq
# first, pliss check folder static on your server, when i

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
# from sklearn.externals.six import StringIO   
from sklearn.tree import _tree 
import pydotplus
import pickle
from datetime import datetime
from bson.objectid import ObjectId

ALLOWED_EXTENSIONS = set(['csv'])

ROOT_PATH = os.environ.get('ROOT_PATH')
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(ROOT_PATH, 'output.log'))
    
# =======SECTION LABEL=======
@app.route('/api/intelligent/all_label', methods=['GET'])
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

def get_label():
  try:
    label = mongo.db.labels
    output = []
    for s in label.find():
      output.append(s['namaLabel'])
    return output
  except :
    return False

def get_solutions(params):
  try:
    solution = mongo.db.solutions.aggregate([
        {
            '$match': {
                'labelIdentity': params
            }
        }
    ])
    output = []
    for s in solution:
      output.append({
        'labelIdentity' : s['labelIdentity'],
        'treatment' : s['treatment'],
        'prevention' : s['prevention']
      })
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

def save_features(colls_name):
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

def get_features():
  try:
    attributes = mongo.db.attributes
    output = []
    for s in attributes.find():
      output.append(s['namaAttribute'])
    return output
  except :
    return False 

def save_labels(data):
  labels_unique = data.Label.unique()
  iteration=0
  mongo.db.labels.drop()
  for i in range(len(labels_unique)):
    d = {
      "namaLabel" : labels_unique[i],
      "labelIdentity" : iteration
    }
    iteration+=1
    mongo.db.labels.insert_one(d)
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

# def create_tree(data_train,feature_cols,model):
#   labels_get = list(map(str,data_train['Label'].unique()))
#   dot_data = StringIO()
#   export_graphviz(model, out_file=dot_data,  
#                   filled=True, rounded=True,
#                   special_characters=True,feature_names = feature_cols,class_names=labels_get)
#   graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
#   graph.write_png("././static/sapi_tree_data.png")

@app.route('/api/intelligent/upload_training_data', methods=['POST'])
def upload_file():
  try:
   file = request.files['file']
   if file and allowed_file(file.filename):
     filename = secure_filename(file.filename)
     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
     data = pd.read_csv("././static/datacobacoba.csv",header=None)
     # GET HEADER
     colls_name = get_header(data)
     # GET ATTRIBUTE
     feature_cols = save_features(colls_name)
     # PRE PROCESSING
     data_training = pre_processing(data,colls_name)
     # TRAINING
     model = training(data_training,feature_cols)
     # SAVE MODEL`
     save_model(model)
    #  create_tree(data_training,feature_cols,model)
     responses = response()
     responses.setStatus(True)
     responses.setMessage("Succesfully save model")
     return jsonify(responses.getResponse())

  except:
    responses = response()
    responses.setStatus(False)
    responses.setMessage("Something wrong :(")
    return jsonify(responses.getResponse())

@app.route('/api/intelligent/test_data', methods=['POST'])
def testing_data():
  # try:
  print("start\n")
  knowledges = mongo.db.pengetahuan
  print("1\n")
  col_solusi = mongo.db.solutions
  print("2\n")
  solusi = []
  print("3\n")
  jawaban_users = request.get_json()
  jawaban_user = []
  jawaban_user.extend(jawaban_users)
  jawaban_user.append({'gejala': 'suhu badan tidak normal','cfuser':'0.4'})
  jawaban_user.append({'gejala': 'detak jantung tidak normal','cfuser':'0.4'}) 
  print("4\n")
  knowledge = []
  print("5\n")
  kemungkinanpenyakits = []
  kemungkinanpenyakit = []
  print("6\n")
  hasil_penyakit = []
  print("7\n")
  hasil_penyakit_final = []
  print("8\n")
  headers = request.args
  print("9\n")
  sapi_id = headers['sapi']
  
  print("tahap 1 mulai \n")
  # tahap 1
  for field in knowledges.find():
        knowledge.append({'_id' : str(field['_id']), 'idpenyakit' : field['label'], 'gejala' : field['idattribute'], 'cf' : field['cfrules'], 'idsolutions' : field['idsolutions']})
  
  for i in range(len(knowledge)):
        for j in range(len(knowledge[i]['gejala'])):
            for k in range(len(jawaban_user)):
                if knowledge[i]['gejala'][j] == jawaban_user[k]['gejala']:
                    if len(kemungkinanpenyakits) == 0:
                       kemungkinanpenyakits.append({ 'idpenyakit' : knowledge[i]['idpenyakit'], 'idgejala' : [knowledge[i]['gejala'][j]], 'cfuser' : [jawaban_user[k]['cfuser']], 'cfrule' : [knowledge[i]['cf'][j]], 'idsolutions' : knowledge[i]['idsolutions'], 'cfperkalian' : []  })
                    else:
                        for l in range(len(kemungkinanpenyakits)):
                            if kemungkinanpenyakits[l]['idpenyakit'] == knowledge[i]['idpenyakit']:
                                kemungkinanpenyakits[l]['idgejala'].append(knowledge[i]['gejala'][j])
                                kemungkinanpenyakits[l]['cfuser'].append(jawaban_user[k]['cfuser'])
                                kemungkinanpenyakits[l]['cfrule'].append(knowledge[i]['cf'][j]) 
                                kemungkinanpenyakits[l]['idsolutions'] = knowledge[i]['idsolutions']
                            elif kemungkinanpenyakits[l-1]['idpenyakit'] != knowledge[i]['idpenyakit']:
                                kemungkinanpenyakits.append({ 'idpenyakit' : knowledge[i]['idpenyakit'], 'idgejala' : [knowledge[i]['gejala'][j]], 'cfuser' : [jawaban_user[k]['cfuser']], 'cfrule' : [knowledge[i]['cf'][j]], 'idsolutions' : knowledge[i]['idsolutions'], 'cfperkalian' : []  })
  for y in range(len(kemungkinanpenyakits)):
    if len(kemungkinanpenyakit) == 0:
      kemungkinanpenyakit.append({ 'idpenyakit' : kemungkinanpenyakits[0]['idpenyakit'], 'idgejala' : kemungkinanpenyakits[0]['idgejala'], 'cfuser' : kemungkinanpenyakits[0]['cfuser'], 'cfrule' : kemungkinanpenyakits[0]['cfrule'], 'idsolutions' : kemungkinanpenyakits[0]['idsolutions'], 'cfperkalian' : []  })
    else:
      if kemungkinanpenyakits[y-1]['idpenyakit'] != kemungkinanpenyakits[y]['idpenyakit']:
         kemungkinanpenyakit.append({ 'idpenyakit' : kemungkinanpenyakits[y]['idpenyakit'], 'idgejala' : kemungkinanpenyakits[y]['idgejala'], 'cfuser' : kemungkinanpenyakits[y]['cfuser'], 'cfrule' : kemungkinanpenyakits[y]['cfrule'], 'idsolutions' : kemungkinanpenyakits[y]['idsolutions'], 'cfperkalian' : []  })
  print("tahap 1 selesai \n")
  
  # tahap 2
  for m in range(len(kemungkinanpenyakit)):
        for n in range(len(kemungkinanpenyakit[m]['idgejala'])):
            hasilkali = float(kemungkinanpenyakit[m]['cfuser'][n]) *  float(kemungkinanpenyakit[m]['cfrule'][n])
            kemungkinanpenyakit[m]['cfperkalian'].append(hasilkali)
  for z in range(len(kemungkinanpenyakit)):
      print(kemungkinanpenyakit[z]['idpenyakit'])
  print("tahap 2 selesai \n")
  
  # tahap 3
  for p in range(len(kemungkinanpenyakit)):
        cfold = 0.0
        for q in range(len(kemungkinanpenyakit[p]['idgejala'])):
            if (len(kemungkinanpenyakit[p]['idgejala'])>=2):
                if (q <= len(kemungkinanpenyakit[p]['idgejala'])-2):
                    cfold =  float(kemungkinanpenyakit[p]['cfperkalian'][q] + kemungkinanpenyakit[p]['cfperkalian'][q+1] * (1 - kemungkinanpenyakit[p]['cfperkalian'][q]))
                    hasil_penyakit.append({'id_penyakit' : kemungkinanpenyakit[p]['idpenyakit'], 'cf' : cfold, 'idsolutions' : kemungkinanpenyakit[p]['idsolutions'] })
            else :
                cfold =  float(kemungkinanpenyakit[p]['cfperkalian'][q] )
                hasil_penyakit.append({'id_penyakit' : kemungkinanpenyakit[p]['idpenyakit'], 'cf' : cfold, 'idsolutions' : kemungkinanpenyakit[p]['idsolutions'] })
  s=0
  for r in range(len(hasil_penyakit)):        
      if (r == 0):
          hasil_penyakit_final.append({'id_penyakit' : hasil_penyakit[r]['id_penyakit'], 'cf' : hasil_penyakit[r]['cf'], 'idsolution' : hasil_penyakit[r]['idsolutions'] })
      else:
          if (hasil_penyakit[r]['cf'] > hasil_penyakit_final[r-(1+s)]['cf']):
              hasil_penyakit_final[r-(1+s)]['id_penyakit'] = hasil_penyakit[r]['id_penyakit']
              hasil_penyakit_final[r-(1+s)]['cf'] = hasil_penyakit[r]['cf']
              hasil_penyakit_final[r-(1+s)]['idsolution'] = hasil_penyakit[r]['idsolutions']
              s+=1
          else:
              s+=1
  for field in col_solusi.find():
    solusi.append({'_id' : str(field['_id']), 'labelIdentity' : field['labelIdentity'], 'treatment' : field['treatment'], 'prevention' : field['prevention']})
  for x in range(len(solusi)):
    if(solusi[x]['_id'] == hasil_penyakit_final[0]['idsolution']):
      hasil_treatment = solusi[x]['treatment']
      hasil_prevention = solusi[x]['prevention']
  
  attributes2 = []
  for i in jawaban_users:
    attributes2.append({
      "namaAttributes" : i['gejala'],
      "nilai" : i['cfuser'],
      "true" : 1
    })
  
  print("\ntahap 3 selesai \n")
  responses = response()
  diagnose_insert = {
    "sapiId" : ObjectId(sapi_id),
    "diagnose" : hasil_penyakit_final[0]['id_penyakit'],
    "gejala" : attributes2, 
    "nilai" : float(hasil_penyakit_final[0]['cf']),
    "tanggal" : datetime.now(),
    "treatment" : hasil_treatment,
    "prevention" : hasil_prevention
  }
  print(diagnose_insert)
  responses.setStatus(True)
  mongo.db.diagnoses.insert_one(diagnose_insert)
  responses.setData(diagnose_insert)
  return jsonify(responses.getResponse())
  # except:
  #   jawaban_user_error = request.get_json()
  #   print(jawaban_user_error)
  #   responses = response()
  #   responses.setStatus(False)
  #   responses.setMessage("Something wrong :(")
  #   return jsonify(responses.getResponse())
    
  # try:
  #   model_testing = {}
  #   model_for_saving = {}
  #   attributes = get_features()
  #   labels = get_label()
  #   d = request.get_json()
  #   headers = request.args
  #   sapi_id = headers['sapi']

  #   for i in range(len(attributes)):
  #     model_testing.update({attributes[i]:[d.get(attributes[i])]})
  #     model_for_saving.update({attributes[i]:d.get(attributes[i])})
    
  #   Z_test = pd.DataFrame(data=model_testing)
  #   with open("pickle_model.pkl", 'rb') as file:
  #     pickle_model = pickle.load(file)
    
  #   result = pickle_model.predict(Z_test)
  #   responses = response()
  #   responses.setStatus(True)
  #   # responses.setData(labels[result[0]])
  #   # Save
  #   attributes2 = []
  #   for i in model_for_saving:
  #     attributes2.append({
  #       "namaAttributes" : i,
  #       "nilai" : model_for_saving[i]
  #     })
  #   res = labels[result[0]]
  #   solu = get_solutions(int(result[0]))
  #   diagnose_insert = {
  #     "sapiId" : ObjectId(sapi_id),
  #     "diagnose" : res,
  #     "gejala" : attributes2, 
  #     "tanggal" : datetime.now(),
  #     "treatment" : solu[0]["treatment"],
  #     "prevention" : solu[0]["prevention"]
  #   }
  #   mongo.db.diagnoses.insert_one(diagnose_insert)
  #   responses.setData(diagnose_insert)
  #   return jsonify(responses.getResponse())

  # except:
  #   responses = response()
  #   responses.setStatus(False)
  #   responses.setMessage("Something wrong :(")
    # return jsonify(responses.getResponse())

@app.route('/api/intelligent/all_attributes', methods=['GET'])
def get_all_attributes():
  try:
    responses = response()
    attribut = mongo.db.attributes
    output = []
    for s in attribut.find():
      output.append(
        { 
          'idAttribute' : s['_id'],
          'namaAttribute' : s['namaAttribute'], 
          'attributeIdentitiy': s['attributeIdentitiy']
        })
    responses.setData(output)
    return jsonify(responses.getResponse())
  except :
    responses = response()
    responses.setStatus(False)
    responses.setMessage("Something wrong :(")
    return jsonify(responses.getResponse())

@app.route('/api/intelligent/all_diagnoses', methods=['GET'])
def get_all_diagnoses():
  try:
    responses = response()
    diagnoses = mongo.db.diagnoses.aggregate([
      {
          '$group': {
              '_id': '$diagnose', 
              'total': {
                  '$sum': 1
              }
          }
      }
    ])
    output = []
    for s in diagnoses:
      output.append(
        {
          'diagnose' : s['_id'], 
          'total': s['total']
        })
    responses.setData(output)
    return jsonify(responses.getResponse())
  except :
    responses = response()
    responses.setStatus(False)
    responses.setMessage("Something wrong :(")
    return jsonify(responses.getResponse())

@app.route('/api/intelligent/all_diagnoses_in_time', methods=['GET'])
def get_all_diagnoses_in_time():
  try:
    responses = response()
    headers = request.args
    start = headers['start']
    end = headers['end']
    start_arr = start.split("-")
    end_arr = end.split("-")
    start_year = int(start_arr[0])
    start_month = int(start_arr[1])
    start_day = int(start_arr[2])
    end_year = int(end_arr[0])
    end_month = int(end_arr[1])
    end_day = int(end_arr[2])
    diagnoses = mongo.db.diagnoses.aggregate([
      {
          '$match': {
              'tanggal': {
                  '$gte': datetime(start_year,start_month,start_day,0,0,0), 
                  '$lte': datetime(end_year,end_month,end_day,0,0,0)
              }
          }
      }, {
          '$group': {
              '_id': '$diagnose', 
              'total': {
                  '$sum': 1
              }
          }
      }
    ])
    output = []
    for s in diagnoses:
      output.append(
        {
          'diagnose' : s['_id'], 
          'total': s['total']
        })
    responses.setData(output)
    return jsonify(responses.getResponse())
  except :
    responses = response()
    responses.setStatus(False)
    responses.setMessage("Something wrong :(")
    return jsonify(responses.getResponse())

@app.route('/api/intelligent/all_gejala', methods=['GET'])
def get_all_gejala():
  try:
    responses = response()
    diagnoses = mongo.db.diagnoses.aggregate([
      {
          '$unwind': {
              'path': '$gejala'
          }
      }, {
          '$group': {
              '_id': '$gejala.namaAttributes', 
              'total': {
                  '$sum': {
                      '$multiply': [
                          '$gejala.true'
                      ]
                  }
              }
          }
      }
    ])
    output = []
    for s in diagnoses:
      output.append(
        {
          'gejala' : s['_id'], 
          'total': s['total']
        })
    responses.setData(output)
    return jsonify(responses.getResponse())
  except :
    responses = response()
    responses.setStatus(False)
    responses.setMessage("Something wrong :(")
    return jsonify(responses.getResponse())

@app.route('/api/intelligent/all_gejala_limit', methods=['GET'])
def get_all_gejala_limit():
  try:
    responses = response()
    diagnoses = mongo.db.diagnoses.aggregate([
      {
          '$unwind': {
              'path': '$gejala'
          }
      }, {
          '$group': {
              '_id': '$gejala.namaAttributes', 
              'total': {
                  '$sum': {
                      '$multiply': [
                          '$gejala.true'
                      ]
                  }
              }
          }
      }, {
          '$sort': {
              'total': -1
          }
      }, {
          '$limit': 5
      }
    ])
    output = []
    for s in diagnoses:
      output.append(
        {
          'gejala' : s['_id'], 
          'total': s['total']
        })
    responses.setData(output)
    return jsonify(responses.getResponse())
  except :
    responses = response()
    responses.setStatus(False)
    responses.setMessage("Something wrong :(")
    return jsonify(responses.getResponse())

@app.route('/api/intelligent/all_gejala_in_time', methods=['GET'])
def get_all_gejala_in_time():
  try:
    responses = response()
    headers = request.args
    start = headers['start']
    end = headers['end']
    start_arr = start.split("-")
    end_arr = end.split("-")
    start_year = int(start_arr[0])
    start_month = int(start_arr[1])
    start_day = int(start_arr[2])
    end_year = int(end_arr[0])
    end_month = int(end_arr[1])
    end_day = int(end_arr[2])
    diagnoses = mongo.db.diagnoses.aggregate([
      {
          '$match': {
              'tanggal': {
                  '$gte': datetime(start_year,start_month,start_day,0,0,0), 
                  '$lte': datetime(end_year,end_month,end_day,0,0,0)
              }
          }
      }, {
          '$unwind': {
              'path': '$gejala'
          }
      }, {
          '$group': {
              '_id': '$gejala.namaAttributes', 
              'total': {
                  '$sum': {
                      '$multiply': [
                          '$gejala.true'
                      ]
                  }
              }
          }
      }
    ])
    output = []
    for s in diagnoses:
      output.append(
        {
          'gejala' : s['_id'], 
          'total': s['total']
        })
    responses.setData(output)
    return jsonify(responses.getResponse())
  except :
    responses = response()
    responses.setStatus(False)
    responses.setMessage("Something wrong :(")
    return jsonify(responses.getResponse())

@app.route('/api/intelligent/all_gejala_in_time_limit', methods=['GET'])
def get_all_gejala_in_time_limit():
  try:
    responses = response()
    headers = request.args
    start = headers['start']
    end = headers['end']
    start_arr = start.split("-")
    end_arr = end.split("-")
    start_year = int(start_arr[0])
    start_month = int(start_arr[1])
    start_day = int(start_arr[2])
    end_year = int(end_arr[0])
    end_month = int(end_arr[1])
    end_day = int(end_arr[2])
    diagnoses = mongo.db.diagnoses.aggregate([
      {
          '$match': {
              'tanggal': {
                  '$gte': datetime(start_year,start_month,start_day,0,0,0), 
                  '$lte': datetime(end_year,end_month,end_day,0,0,0)
              }
          }
      }, {
          '$unwind': {
              'path': '$gejala'
          }
      }, {
          '$group': {
              '_id': '$gejala.namaAttributes', 
              'total': {
                  '$sum': {
                      '$multiply': [
                          '$gejala.true'
                      ]
                  }
              }
          }
      }, {
          '$sort': {
              'total': -1
          }
      }, {
          '$limit': 5
      }
    ])
    output = []
    for s in diagnoses:
      output.append(
        {
          'gejala' : s['_id'], 
          'total': s['total']
        })
    responses.setData(output)
    return jsonify(responses.getResponse())
  except :
    responses = response()
    responses.setStatus(False)
    responses.setMessage("Something wrong :(")
    return jsonify(responses.getResponse())

@app.route('/api/intelligent/diagnoses_by_sapi', methods=['POST'])
def get_diagnoses_by_sapi():
  try:
    headers = request.args
    sapi_id = headers['sapi']
    responses = response()
    diagnoses = mongo.db.diagnoses.aggregate([
      {
          '$match': {
              'sapiId': ObjectId(sapi_id)
          }
      }, {
          '$group': {
              '_id': '$diagnose', 
              'total': {
                  '$sum': 1
              }
          }
      }
    ])
    output = []
    for s in diagnoses:
      output.append(
        {
          'diagnose' : s['_id'], 
          'total': s['total']
        })
    responses.setData(output)
    return jsonify(responses.getResponse())
  except :
    responses = response()
    responses.setStatus(False)
    responses.setMessage("Something wrong :(")
    return jsonify(responses.getResponse())

@app.route('/api/intelligent/diagnoses_by_sapi_in_time', methods=['GET'])
def get_diagnoses_by_sapi_in_time():
  try:
    headers = request.args
    sapi_id = headers['sapi']
    start = headers['start']
    end = headers['end']
    start_arr = start.split("-")
    end_arr = end.split("-")
    start_year = int(start_arr[0])
    start_month = int(start_arr[1])
    start_day = int(start_arr[2])
    end_year = int(end_arr[0])
    end_month = int(end_arr[1])
    end_day = int(end_arr[2])
    responses = response()
    diagnoses = mongo.db.diagnoses.aggregate([
      {
          '$match': {
              '$and': [
                  {
                      'sapiId': ObjectId(sapi_id)
                  }, {
                      'tanggal': {
                          '$gte': datetime(start_year,start_month,start_day,0,0,0), 
                          '$lte': datetime(end_year,end_month,end_day,0,0,0)
                      }
                  }
              ]
          }
      }, {
          '$group': {
              '_id': '$diagnose', 
              'total': {
                  '$sum': 1
              }
          }
      }
    ])
    output = []
    for s in diagnoses:
      output.append(
        {
          'diagnose' : s['_id'], 
          'total': s['total']
        })
    responses.setData(output)
    return jsonify(responses.getResponse())
  except :
    responses = response()
    responses.setStatus(False)
    responses.setMessage("Something wrong :(")
    return jsonify(responses.getResponse())

@app.route('/api/intelligent/gejala_by_sapi', methods=['POST'])
def get_gejala_by_sapi():
  try:
    headers = request.args
    sapi_id = headers['sapi']
    responses = response()
    diagnoses = mongo.db.diagnoses.aggregate([
      {
          '$match': {
              'sapiId': ObjectId(sapi_id)
          }
      }, {
          '$unwind': {
              'path': '$gejala'
          }
      }, {
          '$group': {
              '_id': '$gejala.namaAttributes', 
              'total': {
                  '$sum': {
                      '$multiply': [
                          '$gejala.nilai'
                      ]
                  }
              }
          }
      }
    ])
    output = []
    for s in diagnoses:
      output.append(
        {
          'gejala' : s['_id'], 
          'total': s['total']
        })
    responses.setData(output)
    return jsonify(responses.getResponse())
  except :
    responses = response()
    responses.setStatus(False)
    responses.setMessage("Something wrong :(")
    return jsonify(responses.getResponse())

@app.route('/api/intelligent/gejala_by_sapi_limit', methods=['POST'])
def get_gejala_by_sapi_limit():
  try:
    headers = request.args
    sapi_id = headers['sapi']
    responses = response()
    diagnoses = mongo.db.diagnoses.aggregate([
      {
          '$match': {
              'sapiId': ObjectId(sapi_id)
          }
      }, {
          '$unwind': {
              'path': '$gejala'
          }
      }, {
          '$group': {
              '_id': '$gejala.namaAttributes', 
              'total': {
                  '$sum': {
                      '$multiply': [
                          '$gejala.nilai'
                      ]
                  }
              }
          }
      }, {
          '$sort': {
              'total': -1
          }
      }, {
          '$limit': 5
      }
    ])
    output = []
    for s in diagnoses:
      output.append(
        {
          'gejala' : s['_id'], 
          'total': s['total']
        })
    responses.setData(output)
    return jsonify(responses.getResponse())
  except :
    responses = response()
    responses.setStatus(False)
    responses.setMessage("Something wrong :(")
    return jsonify(responses.getResponse())

@app.route('/api/intelligent/gejala_by_sapi_in_time', methods=['GET'])
def get_gejala_by_sapi_in_time():
  try:
    headers = request.args
    sapi_id = headers['sapi']
    start = headers['start']
    end = headers['end']
    start_arr = start.split("-")
    end_arr = end.split("-")
    start_year = int(start_arr[0])
    start_month = int(start_arr[1])
    start_day = int(start_arr[2])
    end_year = int(end_arr[0])
    end_month = int(end_arr[1])
    end_day = int(end_arr[2])
    responses = response()
    diagnoses = mongo.db.diagnoses.aggregate([
      {
          '$match': {
              '$and': [
                  {
                      'sapiId': ObjectId(sapi_id)
                  }, {
                      'tanggal': {
                          '$gte': datetime(start_year,start_month,start_day,0,0,0), 
                          '$lte': datetime(end_year,end_month,end_day,0,0,0)
                      }
                  }
              ]
          }
      }, {
          '$unwind': {
              'path': '$gejala'
          }
      }, {
          '$group': {
              '_id': '$gejala.namaAttributes', 
              'total': {
                  '$sum': {
                      '$multiply': [
                          '$gejala.nilai'
                      ]
                  }
              }
          }
      }
    ])
    output = []
    for s in diagnoses:
      output.append(
        {
          'gejala' : s['_id'], 
          'total': s['total']
        })
    responses.setData(output)
    return jsonify(responses.getResponse())
  except :
    responses = response()
    responses.setStatus(False)
    responses.setMessage("Something wrong :(")
    return jsonify(responses.getResponse())

@app.route('/api/intelligent/gejala_by_sapi_in_time_limit', methods=['GET'])
def get_gejala_by_sapi_in_time_limit():
  try:
    headers = request.args
    sapi_id = headers['sapi']
    start = headers['start']
    end = headers['end']
    start_arr = start.split("-")
    end_arr = end.split("-")
    start_year = int(start_arr[0])
    start_month = int(start_arr[1])
    start_day = int(start_arr[2])
    end_year = int(end_arr[0])
    end_month = int(end_arr[1])
    end_day = int(end_arr[2])
    responses = response()
    diagnoses = mongo.db.diagnoses.aggregate([
      {
          '$match': {
              '$and': [
                  {
                      'sapiId': ObjectId(sapi_id)
                  }, {
                      'tanggal': {
                          '$gte': datetime(start_year,start_month,start_day,0,0,0), 
                          '$lte': datetime(end_year,end_month,end_day,0,0,0)
                      }
                  }
              ]
          }
      }, {
          '$unwind': {
              'path': '$gejala'
          }
      }, {
          '$group': {
              '_id': '$gejala.namaAttributes', 
              'total': {
                  '$sum': {
                      '$multiply': [
                          '$gejala.nilai'
                      ]
                  }
              }
          }
      }, {
          '$sort': {
              'total': -1
          }
      }, {
          '$limit': 5
      }
    ])
    output = []
    for s in diagnoses:
      output.append(
        {
          'gejala' : s['_id'], 
          'total': s['total']
        })
    responses.setData(output)
    return jsonify(responses.getResponse())
  except :
    responses = response()
    responses.setStatus(False)
    responses.setMessage("Something wrong :(")
    return jsonify(responses.getResponse())

@app.route('/api/intelligent/add_solution', methods=['POST'])
def add_solution():
  try:
    d = request.get_json()
    mongo.db.solutions.insert_one(d)
    responses = response()
    responses.setStatus(True)
    responses.setData(d)
    return jsonify(responses.getResponse())

  except:
    responses = response()
    responses.setStatus(False)
    responses.setMessage("Something wrong :(")
    return jsonify(responses.getResponse())

@app.route('/api/intelligent/all_solutions', methods=['GET'])
def get_all_solutions():
  try:
    responses = response()
    attribut = mongo.db.solutions
    output = []
    for s in attribut.find():
      output.append(
        {
          'labelIdentity' : s['labelIdentity'], 
          'treatment': s['treatment'],
          'prevention': s['prevention']
        })
    responses.setData(output)
    return jsonify(responses.getResponse())
  except :
    responses = response()
    responses.setStatus(False)
    responses.setMessage("Something wrong :(")
    return jsonify(responses.getResponse())