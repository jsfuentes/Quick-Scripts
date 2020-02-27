const utils = require("./utils.js");

function addDateToDoc(d) {
  var date = new Date();

  backupD = {
    ...d,
    date: date.toDateString()
  };
  return backupD;
}

async function backup() {
  const secrets = await utils.readSecrets();
  const dbVideos = await utils.connectToVideos(secrets);
  const dbBackup = await utils.connectToBackup(secrets);

  let companyDoc = await dbVideos.find().toArray();
  console.log("Company Doc", companyDoc);
  companyDoc.forEach(d => {
    delete d["_id"]; //need unique ids, and we want multiple versions in the same db
    dbBackup.insertOne(addDateToDoc(d));
  });

  console.log("Backup complete");
}

backup();
