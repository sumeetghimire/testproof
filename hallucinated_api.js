/**
 * Example script with a hallucinated API call for PRoof detection.
 * fs.readFileSyncAsync does not exist - Node has readFileSync or fs.promises.readFile.
 */
const fs = require('fs');
const data = fs.readFileSyncAsync('/tmp/example.txt', 'utf8');
module.exports = { data };
