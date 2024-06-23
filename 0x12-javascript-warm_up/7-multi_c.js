#!/usr/bin/node

const args = process.argv;

const noofoccs = parseInt(args[2]);

if (isNaN(noofoccs)) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < noofoccs; x++) {
    console.log('C is fun');
  }
}
