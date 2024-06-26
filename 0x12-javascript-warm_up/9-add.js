#!/usr/bin/node
const { argv } = require('node:process');
function add (a, b) {
  if (isNaN(a) || isNaN(b)) console.log(NaN);
  else console.log(a + b);
}
add(parseInt(argv[2]), parseInt(argv[3]));
