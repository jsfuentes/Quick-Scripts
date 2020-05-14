const utils = require("./utils.js");
const ObjectID = require("mongodb").ObjectID;
const nanoid = require("nanoid");

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
  // _id: new ObjectID("jip_JBFj0GX")
  _id: "jip_JBFj0GX"
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

async function testObjectToString() {
  const secrets = await utils.readSecrets();
  const dbData = await utils.connectToDB(secrets, COLLECTION);

  console.log(TEST_QUERY);
  let doc = await dbData.findOne(TEST_QUERY);
  console.log(doc);
  delete doc._id;
  doc._id = nanoid(11);
  await dbData.deleteOne(TEST_QUERY);
  await dbData.insertOne(doc);
}

async function objectIDToString() {
  const secrets = await utils.readSecrets();
  const dbData = await utils.connectToDB(secrets, COLLECTION);

  let docs = await dbData.find().toArray();
  docs.forEach(doc => {
    dbData.deleteOne({ _id: doc._id });
    delete doc._id;
    doc._id = nanoid(11);
    dbData.insertOne(doc);
    console.log(doc);
  });
}

// testBackfill();
// backfillAll();
// testObjectToString();
objectIDToString();
