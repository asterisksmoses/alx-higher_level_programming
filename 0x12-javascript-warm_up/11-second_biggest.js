#!/usr/bin/node

function secondbig (num) {
  let max1 = -Infinity; let max2 = -Infinity;

  num.forEach((num) => {
    const x = parseInt(num);
    if (x > max1) {
      [max2, max1] = [max1, x];
    } else if (x < max1 && x > max2) {
      max2 = x;
    }
  });

  return max2;
}

const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  console.log(secondbig(args));
}
