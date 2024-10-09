#!/usr/bin/node
// Returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let occurence = 0;
  let entry;
  for (entry of list) {
    if (entry === searchElement) { occurence++; }
  }
  return occurence;
};
