#!/usr/bin/node
// A Rectangle class, with print/ diagramatical representation

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    console.log((('X'.repeat(this.width) + '\n').repeat(this.height)).replace(/\n$/, ''));
  }
}

module.exports = Rectangle;
