#!/usr/bin/node

function add (x, y) {
  return x + y;
}

const args = process.argv;

const int1 = parseInt(args[2]);
const int2 = parseInt(args[3]);

console.log(add(int1, int2));
