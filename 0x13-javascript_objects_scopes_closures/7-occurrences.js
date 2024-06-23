#!/usr/bin/node

exports.nbOccurences = function (list, searchEl) {
  let x = 0;
  for (const element of list) {
    if (element === searchEl) {
      x++;
    }
  }

  return x;
};
