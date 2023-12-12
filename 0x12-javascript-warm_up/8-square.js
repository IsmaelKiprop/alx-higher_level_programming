#!/usr/bin/node

const size = parseInt(process.argv[2]);
const myStr = 'X';

if (size) {
  let i = 0;
  while (i < size) {
    console.log(myStr.repeat(size));
    i++;
  }
} else {
  console.log('Missing size');
}
