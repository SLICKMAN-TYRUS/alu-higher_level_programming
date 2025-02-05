#!/usr/bin/node
const request = require('request');
const path = process.argv[2];

request(path, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    let count = 0;
    const result = JSON.parse(body).results;
    for (const item in result) {
      const charac = result[item].characters;
      for (const i in charac) {
        if (charac[i].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
