#!/usr/bin/node
// Take advantage of function->closure->function, to create a base converter

exports.converter = function (base) {
  return function convert (number) {
    if (number === 0) return '0';
    return (convert(Math.floor(number / base)) +
            '0123456789abcdef'[(number % base)]).replace(/^0/, '');
  };
};
