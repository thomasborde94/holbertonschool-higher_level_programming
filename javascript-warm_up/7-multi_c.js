#!/usr/bin/node
let number = parseInt(process.argv[2]);
if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 1; i <= number; i++) {
    console.log('C is fun');
  }
}
