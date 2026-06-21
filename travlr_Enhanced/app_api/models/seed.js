//Bring in the DB connection and the Trip, Story schema
const Mongoose = require('./db');
const {Trip, Story} = require('./travlr');

//Read seed data from JSON file
var fs = require('fs');
var trips = JSON.parse(fs.readFileSync('./data/trips.json', 'utf8')); //Imports trips seed JSON data
var stories = JSON.parse(fs.readFileSync('./data/stories.json', 'utf8')); //Imports stories seed JSON data

// delete any existing records, then add seed data
const seedDB = async () => {
    await Trip.deleteMany({});
    await Story.deleteMany({});

    await Trip.insertMany(trips);
    await Story.insertMany(stories);
};

// Close the MondoDB connection and exit
seedDB().then(async () => {
    await Mongoose.connection.close();
    process.exit(0);
});

