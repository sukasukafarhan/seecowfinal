var mongoose = require('mongoose');
var Schema = mongoose.Schema;
var AttributeSchema = new Schema({
  namaAttribute: {
    type: String,
    required: true
  },
  attributeIdentity : Number
});

module.exports = mongoose.model('Attribute', AttributeSchema);
