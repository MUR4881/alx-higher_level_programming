#!/usr/bin/node
const { argv } = require('node:process');
let n;
if ((isNaN(n = parseInt(argv[2], 10)))) console.log('Not a number');
else console.log(`My number: ${n}`);
