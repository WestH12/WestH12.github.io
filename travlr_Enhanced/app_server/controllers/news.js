const storiesEndpoint = 'http://localhost:3000/api/stories';
const options = {
    method: 'GET',
    headers: {
        'Accept': 'application/json'
    }
}

//var fs = require('fs');
//var stories = JSON.parse(fs.readFileSync('./data/stories.json', 'utf8'));


/* GET news view */
const news = async function (req, res, next) {
    //console.log('NEWS CONTROLLER BEGIN');
    await fetch(storiesEndpoint, options)
        .then((res) => res.json())
        .then((json) => {
            let message = null;
            if (!(json instanceof Array)){
                message = "API lookup error";
            } else {
                if (!json.length){
                    message = "No trips exist in our database";
                }
                 
            }
            //console.log(json);
            res.render('news', {title: "Travlr Getaways", stories: json});
        })
        .catch((err => res.status(500).send(err.message)));
};

module.exports = {
    news
};