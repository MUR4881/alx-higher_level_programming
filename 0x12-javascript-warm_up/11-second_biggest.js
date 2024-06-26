#!/usr/bin/node
const { argv } = require('node:process');
let a, b, c, entry;
let index = 2;// Avoid the process name, the script name
const length = argv.length;
const arr = [];
if (length <= 3) console.log(0);
else { // Searching! for 2nd highest
  while (index < length) {
    entry = parseInt(argv[index]);
    if (!(isNaN(entry))) arr.push(entry);// adding only number
    index++;
  }
  /* Select 1st 2 element, deciding the biggest, now keeping going
   * through the array, and comparing the new element with the 1st
   * and 2nd element
   */
  a = arr[0];
  b = arr[1];
  if (b > a) { c = a; a = b; b = c; } // Swapping
  for (c of arr) {
    if (c > a) { b = a; a = c; } else if ((c > b) && (a !== c)) b = c;
  }
  if (arr.length > 1) console.log(b);
  else console.log(0);
}
