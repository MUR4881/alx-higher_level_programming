#!/usr/bin/node
// Taking advantage of closure in the module context

exports.logMe = function (item) {
  console.log(`${calls}: ${item}`);
  calls++;
};

let calls = 0;
