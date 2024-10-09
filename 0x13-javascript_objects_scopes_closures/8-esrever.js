#!/usr/bin/node
// returns the reversed version of a list

exports.esrever = function (list) {
  let index = list.length - 1;
  const newList = [];
  while (index >= 0) {
    newList.push(list[index]);
    index--;
  }
  return newList;
};
