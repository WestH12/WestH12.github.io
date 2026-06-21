const mongoose = require('mongoose');

// Defining the trip schema
const tripSchema = new mongoose.Schema({
    code: {type: String, required: true, index: true}, 
    name: {type: String, required: true, index: true},
    length: {type: String, required: true},
    start: {type: Date, required: true},
    resort: {type: String, required: true},
    perPerson: {type: String, required: true},
    image: {type: String, required: true},
    description: {type: String, required: true}
});
const Trip = mongoose.model('trips', tripSchema);

// Defining the story schema
const storySchema = ({
    code: {type: String, required: true, index: true}, 
    title: {type: String, required: true},
    image: {type: String, required: true},
    date: {type: String, required: true},
    author: {type: String, required: true, index: true},
    story: {type: String, required: true}
});
const Story = mongoose.model('stories', storySchema);


// Exporting the trip and story schema
module.exports = {
    Trip, 
    Story
};