const fs = require("fs"),
  MongoClient = require("mongodb").MongoClient,
  util = require("util");

module.exports = {
  delay,
  randomDelay,
  readSecrets,
  connectToDB,
  connectToVideos,
  connectToBackup
};

function delay(timeout) {
  return new Promise(resolve => {
    setTimeout(resolve, timeout);
  });
}

function randomDelay() {
  return new Promise(resolve => {
    setTimeout(resolve, Math.floor(Math.random() * 4000) + 777);
  });
}

async function readSecrets() {
  // Convert fs.readFile into Promise version of same
  const readFile = util.promisify(fs.readFile);
  const data = await readFile("secrets.json");
  return JSON.parse(data);
}

async function connectToDB(secrets, name) {
  const db = await MongoClient.connect(secrets["db_uri"], {
    useNewUrlParser: true,
    useUnifiedTopology: true
  });

  const dbo = db.db("sigma");
  return dbo.collection(name);
}

//YES I AM NO COMBINING THESE FUNCTION, WHY? YOU WOULD HAVE TO MAKE A CONSTANT RIGHT, WELL THE CONSTANT IS THIS FUNCTION. DRY ISNT GOD
async function connectToVideos(secrets) {
  return connectToDB(secrets, "videos");
}

async function connectToBackup(secrets) {
  return connectToDB(secrets, "backup");
}
