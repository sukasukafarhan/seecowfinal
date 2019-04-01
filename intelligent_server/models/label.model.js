var mongoose = require('mongoose');
var Schema = mongoose.Schema;
var LabelSchema = new Schema({
  namaLabel: {
    type: String,
    required: true
  },
  attribute: [Schema.Types.Mixed],
  labelIdentity:Number

});

module.exports = mongoose.model('Label', LabelSchema);
