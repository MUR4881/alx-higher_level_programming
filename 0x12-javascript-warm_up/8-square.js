#!/usr/bin/node
const { argv } = require('node:process');
let size2;
let size = size2 = parseInt(argv[2]);
size = size2 = size < 0 ? 0 : size; // Making size zero, if less than
if (isNaN(size)) console.log('Missing size');
else while (size2--) console.log('X'.repeat(size));
