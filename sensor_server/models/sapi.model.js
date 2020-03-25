var mongoose = require('mongoose');
var Schema = mongoose.Schema;
const PerangkatSchema = new Schema({
  idOnRaspi: {
    type: Schema.Types.ObjectId,
  },
  status: Number,
  data: [{
    tanggal:{ type: Date, default: Date.now },
    suhu:Number,
    jantung:Number,
    kondisi:Number,
    x: Number,
    y: Number,
    z: Number,
    position: Number
  }]
});
var SapiSchema = new Schema({
  idPeternak: {
    type: Schema.Types.ObjectId,
  },
  namaSapi: {
    type: String,
    required: true
  },
  perangkat:{
    type: PerangkatSchema,
    required: true
  }
});

module.exports = mongoose.model('Sapi', SapiSchema);
