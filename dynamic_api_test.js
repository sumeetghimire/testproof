/**
 * Dynamic API name test: method name is in a variable.
 * filesystem[fn]("file.txt") where fn = "readFileSyncAsync".
 * readFileSyncAsync does not exist on Node's fs module.
 * Most static analyzers fail here - they only see filesystem[fn], not the actual method name.
 */
const filesystem = require("fs");
const fn = "readFileSyncAsync";

function readFile() {
  return filesystem[fn]("file.txt");
}

module.exports = { readFile };
