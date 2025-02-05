#!/usr/bin/node
const request = require('request');
const path = process.argv[2];

request(path, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const obj = {};
    for (const item of JSON.parse(body)) {
      if (item.completed) {
        if (obj[item.userId]) {
          obj[item.userId]++;
        } else {
          obj[item.userId] = 1;
        }
      }
    }
    console.log(obj);
  }
});
