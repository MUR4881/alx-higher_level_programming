#!/usr/bin/node
// A square class inheriting from Rectangle class

const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    super.print(c);
  }
}

module.exports = Square;
