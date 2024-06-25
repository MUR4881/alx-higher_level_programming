#!/usr/bin/node
const { argv } = require('node:process');
let arg;
let i = -1;
for (arg of argv) {
  i++;
  if (i === 2) {
    console.log(arg);
  }
}
if (i < 2) console.log('No argument');
