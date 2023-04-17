#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const bodyJ = JSON.parse(body);
    const completedTask = {};
    for (let i = 0; i < bodyJ.length; i++) {
      if (bodyJ[i].completed === true) {
        if (completedTask[bodyJ[i].userId] === undefined) {
          completedTask[bodyJ[i].userId] = 0;
        }
        completedTask[bodyJ[i].userId]++;
      }
    }
    console.log(completedTask);
  }
});
