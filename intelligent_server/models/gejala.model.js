var mongoose = require('mongoose');
var Schema = mongoose.Schema;
var GejalaSchema = new Schema({
  namaGejala: {
    type: String,
    required: true
  }
});

module.exports = mongoose.model('Gejala', GejalaSchema);
