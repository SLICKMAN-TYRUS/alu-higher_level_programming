#!/usr/bin/node
const mainSquare = require('./5-square');
module.exports = class square extends mainSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let row = 1; row <= this.height; row++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
