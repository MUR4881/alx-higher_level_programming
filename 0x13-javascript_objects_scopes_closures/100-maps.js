#!/usr/bin/node
// compute new array from imported array
const list = require('./100-data').list;
console.log(list);
console.log(list.map((index, entry) => index * entry));
