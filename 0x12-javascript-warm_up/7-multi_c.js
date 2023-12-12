#!/usr/bin/node

const x = parseInt(process.argv[2]);
if (x) {
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
