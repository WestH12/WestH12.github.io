const request = require('supertest')
const app = require('./app')
const mongoose = require('mongoose')
const {Trip, Story } = require("./app_api/models/travlr")
const User = require("./app_api/models/user")

// Init mockToken variable before assignment in login testing
let mockToken;

// Connects to db, clears all databases, and seeds the Trip and Story DB
beforeAll(async () => {
    await mongoose.connect('mongodb://localhost:27017/travlr-test');

    await Trip.deleteMany({});
    await Trip.create({
        code: 'TEST2026',
        name: 'Test Resort',
        length: '5 Days',
        start: new Date(),
        resort: 'Jest Paradise',
        perPerson: '1111.00',
        image: 'test.jpg',
        description: 'Paradise.'
    });

    await Story.deleteMany({});
    await Story.create({
        "code": "1a2c",
		"image" : "reef2.jpg",
        "title": "Local Reef Expanding Beyonds Predictions",
		"date": "August 12, 2026",
        "author": "Westley Hunter",
		"story" : "A test story to see if I did this correctly."
    });

    await User.deleteMany({});
});

// Tests the /register route by adding a new user
describe('POST /register', () => {
    it('should post a new user to the user database', async () => {
        const newUser = {
            email: 'westley@snhu.edu',
            name: 'admin',
            password: '123'
        };

        const response = await request(app)
        .post('/api/register')
        .send(newUser);

        // Successful test should return 200
        expect(response.statusCode).toBe(200);

    });
});

// Tests the /login route
describe('POST /login', () => {
    it('should verify login credentials and return a token', async () => {
        const user = {
            email: 'westley@snhu.edu',
            name: 'admin',
            password: '123'
        }

        const response = await request(app).post('/api/login').send(user)

        // Captures the login token for future use
        mockToken = response.body;

        // Successful tests should return a 200 and have a defined mockToken
        expect(response.statusCode).toBe(200);
        expect(mockToken).toBeDefined();
    });
});

// Tests getting all the trips from the /trips route
describe('GET /api/trips', () => {
    it('should retrive all trips and return a 200 code', async () => {
        const response = await request(app).get('/api/trips')

        expect(response.statusCode).toBe(200);
        expect(Array.isArray(response.body)).toBe(true);
        expect(response.body.length).toBe(1);
        expect(response.body[0].code).toBe('TEST2026')
    });
});

// Tests getting a specific trip by tripCode
describe('GET /api/trips/:tripCode', () => {
    it('should retrive a trip based on a tripCode and return a 200 code', async () => {
        const response = await request(app).get('/api/trips/TEST2026')

        expect(response.statusCode).toBe(200);
        expect(Array.isArray(response.body)).toBe(true);
        expect(response.body.length).toBe(1);
        expect(response.body[0].code).toBe('TEST2026')
    });
});

// Tests posting a new trip
describe('POST /api/trips', () => {
    it('should post a new trip to the database',async () => {
        const newTrip = {
            code: '2TESTING2',
            name: 'Testingland Resort',
            length: '14 Days',
            start: new Date(),
            resort: 'Supertest Paradise',
            perPerson: '2020.00',
            image: 'test2.jpg',
            description: 'Land of testing fun.'
        }

        // Defining the authHeader from the previously obtained token
        const authHeader = `Bearer ${mockToken}`;

        // Posts the trip, provide authorization token, and sends the new info
        const response = await request(app).post('/api/trips')
        .set('Authorization', authHeader)
        .send(newTrip);

        // Successful tests should return 201, have a matching code, and total db should be length of 2
        expect(response.statusCode).toBe(201);
        expect(response.body.code).toBe('2TESTING2');
        const directDBCheck = await request(app).get('/api/trips');
        expect(directDBCheck.body.length).toBe(2);
    });
});

// Tests the put method
describe('PUT /api/trips/:tripCode', () => {
    it('should update a trip based on a provide tripCode', async() => {
        const update = {
            code: 'TEST2026',
            name: 'Testing Place Town',
            length: '5 Days',
            start: new Date(),
            resort: 'Jest Paradise',
            perPerson: '1111.00',
            image: 'test.jpg',
            description: 'Paradise.'
        }
        // Defining the authHeader from the previously obtained token
        const authHeader = `Bearer ${mockToken}`;

        // Puts the trip with provided tripCode, provide authorization token, and sends the update info
        const response = await request(app).put("/api/trips/TEST2026")
        .set('Authorization', authHeader)
        .send(update);

        // Successful tests should 201
        expect(response.statusCode).toBe(201);

        // Directly checking the DB to ensure there is matching trip
        const directDBCheck = await Trip.findOne({code: 'TEST2026'});
        expect(directDBCheck.name).toBe('Testing Place Town');
    })
});

// Tests deleting a trip
describe('DELETE /api/trips/:tripCode', () =>{
    it('should delete a trip based on a provide tripCode', async () => {
        const authHeader = `Bearer ${mockToken}`;
        const response = await request(app).delete('/api/trips/2TESTING2')
        .set('Authorization', authHeader)

        // Successful tests should return 201 and the DB should no have a trip matching the delete code
        expect(response.statusCode).toBe(201);
        const directDBCheck = await Trip.findOne({'code': '2TESTING2'})
        expect(directDBCheck).toBeNull();

    });
});

// Tests getting all stories 
describe('GET /api/stories', () => {
    it('should retrive all stories and return a 200 code', async () => {
        const response = await request(app).get('/api/stories')

        expect(response.statusCode).toBe(200);
        expect(Array.isArray(response.body)).toBe(true);
        expect(response.body.length).toBe(1);
        expect(response.body[0].code).toBe('1a2c')
    });
});

// Tests getting a specific story by storyCode
describe('GET /api/stories/:storyCode', () => {
    it('should GET a stored based on a provide storyCode', async() => {
        
        const authHeader = `Bearer ${mockToken}`;
        const response = await request(app).get("/api/stories/1a2c");

        expect(response.statusCode).toBe(200);
        expect(response.body[0].title).toBe("Local Reef Expanding Beyonds Predictions")
    })
});

// Resetting the db after all tests to ensure clean future tests
afterAll(async () => {
    await mongoose.connection.db.dropDatabase();
    await mongoose.connection.close();
});