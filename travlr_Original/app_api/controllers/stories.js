const mongoose = require('mongoose');
const {Story} = require('../models/travlr'); // Register model
const Model = mongoose.model('stories');

// GET: /stories - lists all the stories
// Res will include a HTML code and JSON message, regardless of outcome
const storiesList = async(req, res) => {
    const q = await Model
    .find({}) //No filter, return all records
    .exec();

    if (!q) {
        return res
                .status(404)
                .json(err);
    } else {
        return res
                .status(200)
                .json(q);
    }
};

// GET: /stories/storiesCode - finds one story
const storiesFindByCode = async(req, res) => {
    const q = await Model
    .find({'code': req.params.storyCode}) // Return single record
    .exec();

    if (!q) {
        return res
                .status(404)
                .json(err);
    } else {
        return res
                .status(200)
                .json(q);
    }
};

module.exports = {
    storiesList,
    storiesFindByCode
}