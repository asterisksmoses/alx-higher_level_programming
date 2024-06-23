#!/usr/bin/node

function factorial (x) {
  if (x === 0 || isNaN(x)) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}

const args = process.argv;

const num = parseInt(args[2]);

console.log(factorial(num));
