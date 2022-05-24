name = "Express Router Boilerplate"
prefix = "myroute"
code = """import React from "react";
const debug = require("debug")("app:FormWithHeader");

interface FormWithHeaderProps {
  event: SlingShowEvent;
  onlyShowOnEditPath?: boolean;
  afterSave?: ((newEvent: SlingShowEvent) => Promise<void>) | null;
  isCreate?: boolean;
  onClose?: () => void;
  onJoin?: () => void;
  insideSession: boolean;
}

export default function FormWithHeader(props: FormWithHeaderProps) {
  return <div></div>;
}
"""

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

