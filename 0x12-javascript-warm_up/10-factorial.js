#!/usr/bin/node
const { argv } = require('node:process');
const n = parseInt(argv[2]);
function factRecurse (a) {
  if (a <= 1 || isNaN(a)) return (1);
  return (a * factRecurse(a - 1));
}
console.log(factRecurse(n));
