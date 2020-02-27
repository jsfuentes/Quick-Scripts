const utils = require("./utils.js");

const COLLECTION = "videos";

///////////////////////
//EDIT updateDoc to determine how to update
//////////////////////
function updateDoc(d) {
  if (d.s3_url) {
    d.mux_asset_url = d.s3_url;
  }

  return d;
}

const TEST_QUERY = {
  filename: "5e573491e97d08453fe089c1/2020-02-27T03:23:16.638Z-video.webm"
};
async function testBackfill() {
  const secrets = await utils.readSecrets();
  const dbData = await utils.connectToDB(secrets, COLLECTION);

  let doc = await dbData.findOne(TEST_QUERY);
  const newDoc = updateDoc(doc);
  dbData.updateOne(TEST_QUERY, { $set: newDoc });

  console.log("Backfill of", doc, "complete");
}

async function backfillAll() {
  const secrets = await utils.readSecrets();
  const dbData = await utils.connectToDB(secrets, COLLECTION);

  let docs = await dbData.find().toArray();
  docs.forEach(d => {
    const query = { _id: d._id };
    const newDoc = updateDoc(d);
    dbData.updateOne(query, { $set: newDoc });
  });

  console.log("Backfill All complete");
}

// testBackfill();
backfillAll();
