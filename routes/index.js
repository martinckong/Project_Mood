var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res) {
    var db = req.db;
    var collection = db.get('tonevalues');
    collection.find({},{},function(e,docs){
        res.render('index', {
            "tonevalues" : docs
        });
    });
});

router.get('/newsong', function(req, res) {
    res.render('addSong', { title: 'Add New Song' });
});

router.post('/addSong', function(req, res) {
  var db = req.db;

  var song = req.body.Song;
  var artist = req.body.Artist;
  var anger = req.body.Anger;
  var disgust = req.body.Disgust;
  var joy = req.body.Joy;
  var fear = req.body.Fear;
  var sadness = req.body.Sadness;

  var collection = db.get('tonevalues');

  collection.insert({
    "Song" : song,
    "Artist": artist,
    "Anger": anger,
    "Disgust": disgust,
    "Joy": joy,
    "Fear" : fear,
    "Sadness" : sadness
  }, function (err, doc) {
    if(err) {
      res.send("There was a problem adding information");
    }
  });
});
module.exports = router;
