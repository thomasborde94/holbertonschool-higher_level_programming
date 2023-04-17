#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
let count = 0;
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const bodyJ = JSON.parse(body);
    const results = bodyJ.results;
    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].search('18') > 0) {
          count++;
        }
      }
    }
  }
  console.log(count);
});
