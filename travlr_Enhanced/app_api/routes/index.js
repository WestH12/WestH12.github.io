const express = require('express');
const router = express.Router();
const jwt = require('jsonwebtoken');


const tripsController = require('../controllers/trips');
const storiesController = require('../controllers/stories');
const authControler = require('../controllers/authentication');

//Method to authenticate our JWT
function autheticateJWT(req, res, next) {
    //console.log('In Middleware);

    const authHeader = req.headers['authorization'];

    if (authHeader == null){
        console.log('Auth Header Required but Not Present!');
        return res.sendStatus(401);
    }

    let headers = authHeader.split(' ');
    if (headers.length < 1){
        console.log('Not enough tokens in Auth Header: ' + headers.length);
        return res.sendStatus(501);
    }

    const token = authHeader.split(' ')[1];

    if(token == null){
        console.log('Null Bearer Token');
        return res.sendStatus(401);
    }

    const verified = jwt.verify(token, process.env.JWT_SECRET, (err, verified) => {
        if (err) {
            return res.sendStatus(401).json('Token Validation Error!');
        }
        req.auth = verified; // Set the auth param to the decoded object
    });
    next();
};

router.route('/register').post(authControler.register);

// Define route for login endpoint
router
    .route('/login')
    .post(authControler.login);

// Routes for trip methods
router // GET Method routes tripsList
.route('/trips')
.get(tripsController.tripsList)
.post(autheticateJWT, tripsController.tripsAddTrip); //POST Method Adds a Trip

router // GET method routes tripsFindByCode - requires parameter
.route('/trips/:tripCode')
.get(tripsController.tripsFindByCode)
.put(autheticateJWT, tripsController.tripsUpdateTrip)
.delete(autheticateJWT, tripsController.tripsDeleteTrip);

// Routes for story methods
router //GET Method for storiesList route
    .route('/stories')
    .get(storiesController.storiesList);

router // GET Method for storiesFindByCode route - requires parameter
    .route('/stories/:storyCode')
    .get(storiesController.storiesFindByCode);


// Exports router
module.exports = router;