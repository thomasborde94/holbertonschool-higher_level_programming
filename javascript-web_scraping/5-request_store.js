#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const store = process.argv[3];

request(url, 'utf-8', function (err, response, body) {
  if (!err) {
    fs.writeFileSync(store, body);
  }
});
