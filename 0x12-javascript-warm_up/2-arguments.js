#!/usr/bin/node
let myStr;

if (process.argv.length < 3) {
  myStr = 'No argument';
} else if (process.argv.length === 3) {
  myStr = 'Argument found';
} else {
  myStr = 'Arguments found';
}
console.log(myStr);
