''' controller and routes for label '''
import os
from flask import request, jsonify
from app import app, mongo
import logger
from app.schemas.label import validate_label
from app.services.response import response
from werkzeug.utils import secure_filename
import pandas as pd

ALLOWED_EXTENSIONS = set(['csv'])

ROOT_PATH = os.environ.get('ROOT_PATH')
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(ROOT_PATH, 'output.log'))
    
def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/intelligent/upload_training_data', methods=['POST'])
def upload_file():
  if 'file' not in request.files:
    return "no file"
  
  file = request.files['file']
  if file and allowed_file(file.filename):
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    col_names = ['Ambing dan puting bengkak', 'Susus berubah warna', 'Sapi kesakitan bila ambing dipegang', 'Ambing keras dan panas bila dipegang',
'Sisi perut sebelah kiri membesar','Lambung bila dipukul berbunyi seperti drum','Tidak nafsu makan','Gelisah','Air ludah banyak berbuih dan ngiler',
'Adanya lepuh lepuh pada gusi,lidah,sekitar kuku dan di ambing susu','Suhu tubuh tinggi','Bengkak di daerah leher,dada,sisi lambung,pinggang dan alat kelamin luar',
'Pendarahan pada dubur,mulut,hidung, dan urin bercampur darah','Menanduk benda di sekitarnya','Keguguran pada umur kebuntingan 5-8 bulan','Keluar cairan keruh saat keguguran',
'Produksi susu menurun','Kulit di bawah mata kuning','Abortus atau keguguran terjadi selama1-3 minggu','Urin berwarna merah gelap hampir hitam','Kejang kejang',
'Terdapat luka di sapi','Menggaruk atau menggesek tubuhnya','Ada kerak atau kopeng pada permukaan kulit','Bulu rontok','label']
    pima = pd.read_csv("././static/data_dari_koleksi_2.csv", header=None, names=col_names)
    return pima['label']
