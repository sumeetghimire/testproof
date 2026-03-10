/**
 * Alias hallucination test: filesystem is an alias for require("fs").
 * readFileSyncAsync() does not exist on Node's fs module.
 * A weak detector only matches fs.* and misses filesystem.readFileSyncAsync().
 */
const filesystem = require("fs");

function readFile() {
  return filesystem.readFileSyncAsync("data.txt");
}

module.exports = { readFile };
