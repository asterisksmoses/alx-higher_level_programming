#!/usr/bin/node

const args = process.argv;

const size = parseInt(args[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < size; x++) {
    let row = '';
    for (let y = 0; y < size; y++) {
      row += 'X';
    }
    console.log(row);
  }
}
