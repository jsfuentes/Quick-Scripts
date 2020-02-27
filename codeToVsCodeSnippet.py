name = "Express Router Boilerplate"
prefix = "myroute"
code = """const express = require("express");
const debug = require("debug")("app:routes:folder");

const Folder = require("../models/Folder.js");
const asyncH = require("../utils/asyncHandler.js");

let router = express.Router();

router.get("/", asyncH(getFolder));
router.post("/", asyncH(postFolder));

//Returns all users rn
async function getFolder(req, res) {
  const f = await Folder.find().exec();
  debug(f, typeof f);
  res.json(f);
}

async function postFolder(req, res) {
  debug("Post", req.body);
  const newFolder = new Folder(req.body);
  const folder = await newFolder.save();
  res.json(folder);
}

module.exports = router;"""

def cleanLine(l):
  newL = "\t\t\""
  for c in l:
    if c == "\"":
      newL += "\\"
      newL += c
    elif c == "\t":
      newL += "\\t"
    else:
      newL += c
  newL += "\","
  return newL

bs = "{"
be = "}"
print(f"\"{name}\": {bs}")
print(f"\t\"prefix\": \"{prefix}\",")
print("\t\"body\": [")
for line in code.split("\n"):
  print(cleanLine(line))
print("\t]")
print(be + ",")

