/**
 * Dummy JS file to trigger PRoof hallucination check.
 * readFileSyncAsync does not exist on fs - should be readFileSync or fs.promises.readFile.
 */
const fs = require('fs');
const data = fs.readFileSyncAsync('/tmp/foo.txt', 'utf8');
