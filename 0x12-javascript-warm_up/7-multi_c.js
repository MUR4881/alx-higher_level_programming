#!/usr/bin/node
const { argv } = require('node:process');
let n = parseInt(argv[2]);
if (!(isNaN(n)) && n < 0) n = 0;
if (!isNaN(n)) while (n--) console.log('C is fun');
else console.log('Missing number of occurrences');
