var mongoose = require('mongoose');
var Schema = mongoose.Schema;
var KnowledgeSchema = new Schema({
    idLabel: {
        type: Schema.Types.ObjectId,
      },
    attribute: [Schema.Types.Mixed]
});

module.exports = mongoose.model('Label', LabelSchema);
