#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  const arg = process.argv.slice(2);
  arg.sort(function (a, b) { return b - a; });
  console.log(arg[1]);
}
